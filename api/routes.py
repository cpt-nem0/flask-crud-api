from api import app, db

from flask import request, Response, jsonify

from bson.json_util import dumps
from bson.objectid import ObjectId

from typing import Optional


@app.route("/")
def check():
    """To verify is the server is running"""

    return Response(response=dumps({'msg': 'API running 😁😁'}),
                    status=200,
                    mimetype='application/json')


# CREATE
@app.route('/add_product/', methods=['POST'])
def add_product():
    """To insert data into collection"""

    _json = request.json  # user request in json form

    if request.method == 'POST' and _json:
        db.products.insert(_json)

        resp = dumps({'msg': 'Product Added!!'})
        return Response(response=resp, 
                        status=200, 
                        mimetype='application/json')
    else:
        return not_found()


# READ
@app.route('/products/', methods=['GET'])   # get all products
@app.route('/products/<product_id>', methods=['GET'])   # get a single product by id
def list_products(product_id: Optional[str] = None):
    """To get the list of all products"""

    if product_id is not None:
        product = db.products.find({'_id': ObjectId(product_id)})
        resp = dumps(product)
        return resp

    products = db.products.find()   # list of all products from collection
    resp = dumps(products)
    return resp


# UPDATE
@app.route('/update_product/<product_id>', methods=['PUT'])
def update_product(product_id: str):
    """To update a product"""

    _json = request.json

    if _json:
        db.products.update(
            {'_id': ObjectId(product_id)},
            {'$set': _json})

        resp = dumps({'msg': 'Product Updated'})
        return Response(response=resp, 
                        status=200, 
                        mimetype='application/json')

    else:
        not_found()


# DELETE
@app.route('/delete_product/<product_id>', methods=['DELETE'])
def delete_product(product_id: str):
    """To delete a product"""

    db.products.delete_one({'_id': ObjectId(product_id)})

    resp = dumps({'msg': 'Product Deleted!!'})
    return Response(response=resp, 
                    status=200, 
                    mimetype='application/json')

@app.errorhandler(404)
def not_found(error=None):
    """For handling error"""

    msg = {
        'status_code': 404,
        'message': 'Nothing Found!! 😿😿'
    }

    resp = dumps(msg)
    return Response(response=resp, 
                    status=404, 
                    mimetype='application/json')


# Bonus:

# Task1 -
@app.route('/count_discounted_products', methods=['GET'])
def discounted_products():
    """How many products have a discount on them?"""

    dis_products = db.products.find(
        {'$where': "this.regular_price_value > this.offer_price_value"})
    print(dis_products)
    resp = jsonify({'Product with discount': dis_products.count()})
    print(resp)
    resp.status_code = 200
    return resp


# Task2
@app.route('/list_unique_brands', methods=['GET'])
def unique_brands():
    """How many unique brands are present in the collection?"""

    brands = db.products.distinct('brand_name')

    resp = dumps(brands)
    return resp


# Task 3
@app.route('/count_high_offer_price', methods=['GET'])
def high_offer_price():
    """How many products have offer price greater than 300?"""

    total_count = db.products.count({'offer_price_value': {'$gt': 300}})

    resp = jsonify({'Product with offer price > 300': total_count})
    resp.status_code = 200
    return resp


# Task 4
@app.route('/count_high_discount', methods=['GET'])
def high_discount():
    """How many products have discount % greater than 30%?"""

    discount = "(100 * (this.regular_price_value - this.offer_price_value) / this.regular_price_value)"
    products = db.products.find(
        {'$where': f"{discount} > 30"})

    resp = jsonify({'Product with discount greater than 30': products.count()})
    resp.status_code = 200
    return resp
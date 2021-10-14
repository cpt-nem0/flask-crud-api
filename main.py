import json

from api import app, db


def init_database():
    if 'products' not in db.list_collection_names() \
        or db.products.estimated_document_count() == 0:
        with open('data.json', 'r') as file:
            data = json.load(file)
            db.products.insert_many(data)
    print('database initialized')


if __name__ == '__main__':
    init_database()
    app.run(debug=True)

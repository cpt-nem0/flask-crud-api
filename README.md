# flask-crud-api

## How to run this API

**step1:**
To run the the API locally, you need following stuff:
 - [Python](https://www.python.org/downloads/)
 - [MongoDB](https://www.mongodb.com/try/download/community)
 - [Docker](https://www.docker.com/products/docker-desktop) (optional: if you don't want to use docker)

**step2:**
next, step 'clone this repo'

```git clone https://github.com/cpt-nem0/flask-crud-api.git```

**step3:**
Now, add an **environment variable** named "MONGO_URI"
with the mongouri in it.

**step4:**
now, run the ```.\run.ps1``` file in **Powershell** 
this will create your virtual environment and start the server for API.

That's it now you can test the API running locally on you system. the api will be up locally on:

```http://127.0.0.1:5000/```


### For Dokcer users:
Just run ```docker-compose up```  in the main directory

and then the api will be up locally on:

```http://127.0.0.1:5000/```

for testing, use the below endpoints to work with it


## API endpoints


| Endpoint | Request | Description|
| ----------- | ----------- | ----------- | 
|  / | GET | To check if the API is running or not |
| /add_product | POST | To add new product, takes **raw json data** |
| /products | GET | List out all the products. |
| /products/<product_id> | GET | Get the product by it's *product_id* |
| /update_product/<product_id> | PUT | To update an existing product, it takes **raw json data** |
| /delete_product/<product_id> | DELETE | To delete a new product|
| /count_discounted_products | GET | To add new product |
| /list_unique_brands | GET | To add new product |
| /count_high_offer_price | GET | To add new product |
| /count_high_discount | GET | To add new product |

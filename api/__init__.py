import os
import pymongo

from flask import Flask
from pymongo import MongoClient

from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

try:
    # conn = MongoClient('mongodb://localhost:27017')
    conn = MongoClient(os.getenv('MONGO_URI'))
    print('Connected to MongoDB')
except pymongo.errors.ConnectionFailure as e:
    print(f'ERROR: {e}')

db = conn.greendeck_task

from api import routes
from pymongo import MongoClient
from mongoengine import connect

URI = "mongodb://localhost:27018"


def get_mongodb():
    client = MongoClient(URI)

    db = client.qp
    return db




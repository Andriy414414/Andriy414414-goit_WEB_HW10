from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://localhost:27018")

    db = client.qp
    return db

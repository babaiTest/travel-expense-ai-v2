from pymongo import MongoClient

from app import config

client = MongoClient(config.MONGODB_CONNECTION_STRING)

database = client[config.MONGODB_DATABASE]

document_collection = database[
    config.MONGODB_DOCUMENT_COLLECTION
]

travel_collection = database[
    config.MONGODB_TRAVEL_COLLECTION
]
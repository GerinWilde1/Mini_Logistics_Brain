from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # change if using Atlas
db = client["package_tracker"]
collection = db["packages"]
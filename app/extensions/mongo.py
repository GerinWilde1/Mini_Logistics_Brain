from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["logistics_db"]

package_collection = db["packages"]
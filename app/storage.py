from .db import collection

def save_package(package):
   return collection.insert_one(package)

def get_package(package_id):
    return collection.find_one({"id": package_id})

def update_package(package_id, updates):
    collection.update_one(
        {"id": package_id},
        {"$set": updates}
    )

def count_packages():
    return collection.count_documents({})
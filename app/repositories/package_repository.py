from app.extensions import collection

def insert_package(package):
    return collection.insert_one(package)

def find_by_id(package_id):
    return collection.find_one({"id": package_id})

def update_by_id(package_id, updates):
    return collection.update_one({"id": package_id}, {"$set": updates})

def count():
    return collection.count_documents({})

def find_all(status=None):
    query = {}
    if status:
        query["status"] = status

    return list(collection.find(query))
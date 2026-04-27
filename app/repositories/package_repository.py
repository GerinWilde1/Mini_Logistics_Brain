from app.extensions.mongo import package_collection

def insert_package(data):
    package_collection.insert_one(data)

def find_by_id(package_id):
    return package_collection.find_one({"id": package_id})

def find_all(status=None, skip=0, limit=10):
    query = {"status": status} if status else {}

    return list(
        package_collection
        .find(query)
        .skip(skip)
        .limit(limit)
    )

def count_all():
    return package_collection.count_documents({})

def count_by_status():
    pipeline = [
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]
    results = list(package_collection.aggregate(pipeline))
    return {r["_id"]: r["count"] for r in results}

def update_package(package_id, updates):
    package_collection.update_one(
        {"id": package_id},
        {"$set": updates}
    )
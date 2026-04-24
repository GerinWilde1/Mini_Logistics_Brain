from app.extensions import collection

def insert_package(package):
    return collection.insert_one(package)

def find_by_id(package_id):
    return collection.find_one({"id": package_id})

def update_by_id(package_id, updates):
    return collection.update_one({"id": package_id}, {"$set": updates})

def count():
    return collection.count_documents({})

def find_all(status=None, page=1, limit=10):
    query = {}
    if status:
        query["status"] = status

    cursor = collection.find(query) \
        .skip((page - 1) * limit) \
        .limit(limit)

    results = []
    for doc in cursor:
        doc["_id"] = str(doc["_id"])
        results.append(doc)

    return results


def count_all():
    return collection.count_documents({})


def count_by_status():
    pipeline = [
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]

    results = list(collection.aggregate(pipeline))
    return {r["_id"]: r["count"] for r in results}
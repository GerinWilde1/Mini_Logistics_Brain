from .models import Package
from datetime import datetime, timezone
from .storage import save_package, get_package as fetch_package, update_package, count_packages


def serialize(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

VALID_TRANSITIONS = {
    "CREATED": ["IN_TRANSIT"],
    "IN_TRANSIT": ["OUT_FOR_DELIVERY"],
    "OUT_FOR_DELIVERY": ["DELIVERED"],
    "DELIVERED": []
}

def create_package(data):
    package_id = str(count_packages() + 1)

    package = {
        "id": package_id,
        "status": "CREATED",
        "location": data.get("location", "Warehouse"),
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    result = save_package(package)

    # 👇 fetch it back so it includes _id
    saved = fetch_package(package_id)
    saved["_id"] = str(saved["_id"])

    return serialize(saved)

def get_package(package_id):
    package = fetch_package(package_id)
    return serialize(package)

def update_status(package_id, new_status):
    package = fetch_package(package_id)

    if not package:
        return {"error": "Package not found"}

    if new_status not in VALID_TRANSITIONS[package["status"]]:
        return {"error": "Invalid transition"}

    updates = {
        "status": new_status,
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    update_package(package_id, updates)
    return fetch_package(package_id)


def update_location(package_id, new_location):
    package = fetch_package(package_id)

    if not package:
        return {"error": "Package not found"}

    if package["status"] == "DELIVERED":
        return {"error": "Cannot update location of a delivered package"}

    if not new_location:
        return {"error": "Invalid location"}

    updates = {
        "location": new_location,
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    update_package(package_id, updates)
    updated = fetch_package(package_id)
    updated["_id"] = str(updated["_id"])

    return updated
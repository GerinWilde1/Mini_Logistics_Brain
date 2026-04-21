from .models import Package
from .storage import packages
from .storage import save_package, get_package as fetch_package
from datetime import datetime, timezone

VALID_TRANSITIONS = {
    "CREATED": ["IN_TRANSIT"],
    "IN_TRANSIT": ["OUT_FOR_DELIVERY"],
    "OUT_FOR_DELIVERY": ["DELIVERED"],
    "DELIVERED": []
}

def create_package(data):
    package_id = str(len(packages) + 1)

    package = Package(
        id=package_id,
        status="CREATED",
        location=data.get("location", "Warehouse")
    )

    save_package(package)

    print("AFTER CREATE:", packages)  # 👈 add this

    return package.to_dict()

def get_package(package_id):
    package = fetch_package(package_id)
    return package.to_dict() if package else None

def update_status(package_id, new_status):
    print("BEFORE UPDATE:", packages)  # 👈 add this

    package = fetch_package(package_id)

    if not package:
        return {"error": "Package not found"}

    if new_status not in VALID_TRANSITIONS[package.status]:
        return {"error": "Invalid transition"}

    package.status = new_status
    return package.to_dict()


def update_location(package_id, new_location):
    package = fetch_package(package_id)

    if not package:
        return {"error": "Package not found"}

    # Rule: delivered packages are frozen in time ❄️
    if package.status == "DELIVERED":
        return {"error": "Cannot update location of a delivered package"}

    if not new_location:
        return {"error": "Invalid location"}

    package.location = new_location
    package.updated_at = datetime.now(timezone.utc)

    return package.to_dict()
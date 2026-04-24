from datetime import datetime, timezone
from app.repositories import package_repository as repo
from app.utils import serialize
import uuid

VALID_TRANSITIONS = {
    "CREATED": ["IN_TRANSIT"],
    "IN_TRANSIT": ["OUT_FOR_DELIVERY"],
    "OUT_FOR_DELIVERY": ["DELIVERED"],
    "DELIVERED": []
}

def create_package(data):
    package = {
        "id": str(uuid.uuid4()),
        "status": "CREATED",
        "location": data.get("location", "Warehouse"),
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    repo.insert_package(package)
    saved = repo.find_by_id(package["id"])
    return serialize(saved)


def get_packages(status=None, page=1, limit=10):
    return repo.find_all(status, page, limit)

def get_metrics():
    total = repo.count_all()
    by_status = repo.count_by_status()

    return {
        "total_packages": total,
        "by_status": by_status
    }


def update_status(package_id, new_status):
    package = repo.find_by_id(package_id)

    if not package:
        return None, "not_found"

    if new_status not in VALID_TRANSITIONS[package["status"]]:
        return None, "invalid_transition"

    updates = {
        "status": new_status,
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

    repo.update_by_id(package_id, updates)
    return serialize(repo.find_by_id(package_id)), None

def list_packages(status=None):
    packages = repo.find_all()

    if status:
        packages = [p for p in packages if p["status"] == status]

    return [serialize(p) for p in packages]

def count_packages():
    return repo.count()


def get_metrics():
    return {
        "total": repo.count_all(),
        "by_status": repo.count_by_status()
    }
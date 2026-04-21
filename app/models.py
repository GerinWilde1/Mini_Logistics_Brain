from datetime import datetime, timezone

class Package:
    def __init__(self, id, status, location):
        self.id = id
        self.status = status
        self.location = location
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "location": self.location,
            "updated_at": self.updated_at.isoformat()
        }
from datetime import datetime

class Package:
    def __init__(self, id, status, location):
        self.id = id
        self.status = status
        self.location = location
        self.updateed_at = datetime.timezone_aware()

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "location": self.location,
            "updated_at": self.updateed_at.isoformat()
        }

from datetime import datetime

from bson.objectid import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class ShanyraqsRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyraq(self, user_id, user: dict):
        payload = {
            "type": user["type"],
            "price": user["price"],
            "address": user["address"],
            "area": user["area"],
            "rooms_count": user["rooms_count"],
            "description": user["description"],
            "created_at": datetime.utcnow(),
            "user_id": user_id,
        }

        self.database["shanyraqs"].insert_one(payload)

    def get_shanyraq_by_id(self, user_id: str) -> dict | None:
        user = self.database["shanyraqs"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    def get_shanyraqs_by_email(self, email: str) -> dict | None:
        user = self.database["shanyraqs"].find(
            {
                "email": email,
            }
        )
        return user

    def update_shanyraq(self, user_id: str, data: dict):
        self.database["shanyraqs"].update_one(
            filter={"_id": ObjectId(user_id)},
            update={
                "$set": {
                    "type": data["type"],
                    "price": data["price"],
                    "address": data["address"],
                    "area": data["area"],
                    "rooms_count": data["rooms_count"],
                    "description": data["description"],
                }
            },
        )

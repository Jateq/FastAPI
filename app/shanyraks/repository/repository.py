# from datetime import datetime
# from typing import Optional

from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, shanyrak: dict):
        payload = {
            "type": shanyrak["type"],
            "price": shanyrak["price"],
            "address": shanyrak["address"],
            "area": shanyrak["area"],
            "rooms_count": shanyrak["rooms_count"],
            "description": shanyrak["description"],
            "user_id": ObjectId(shanyrak["user_id"])
        }

        shanyrak = self.database["shanyraks"].insert_one(payload)
        return shanyrak.inserted_id
    
    def get_shanyrak_by_id(self, shanyrak_id: str):
        shanyrak = self.database["shanyraks"].find_one(
            {"_id": ObjectId(shanyrak_id)}
        )
        return shanyrak
    
    def update_shanyrak(self, shanyrak_id : str, user_id: str, shanyrak: dict):
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)},
            update={
                "$set": {
                    "type": shanyrak["type"],
                    "price": shanyrak["price"],
                    "address": shanyrak["address"],
                    "area": shanyrak["area"],
                    "rooms_count": shanyrak["rooms_count"],
                    "description": shanyrak["description"],
                }
            },
        )
        
    def delete_shanyrak(self, shanyrak_id : str, user_id):
        result = self.database["shanyraks"].delete_one({"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)})
        
    def create_media(self, shanyrak_id : str, user_id, result):
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)},
            update={
                "$set": {
                    "media": result,
                }
            },
        )
        
    def delete_media(self, shanyrak_id : str, user_id, must_delete : list):
        shanyrak = self.database["shanyraks"].find_one(
            {"_id": ObjectId(shanyrak_id)}
        )
        media_list = shanyrak["media"]
        filtered_media = [item for item in media_list if item not in must_delete]
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)},
            update={
                "$set": {
                    "media": filtered_media,
                }
            },
        )
    
    
    def create_comment(self, shanyrak_id : str, comment):
        comment["_id"] = ObjectId()
        self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(shanyrak_id)},
            update={
                "$push": {
                    "comments": comment,
                }
            },
        )
        
    def get_comments(self, shanyrak_id):
        shanyrak = self.database["shanyraks"].find_one(
            {"_id": ObjectId(shanyrak_id)}
        )
        return shanyrak["comments"]
    
    # def patch_comment(self, shanyrak_id, comment_id):
    #     self.database["shanyraks"].update_one(
    #         filter={"_id": ObjectId(shanyrak_id), "user_id": ObjectId(user_id)},
    #         update={
    #             "$set": {
    #                 "type": shanyrak["type"],
    #                 "price": shanyrak["price"],
    #                 "address": shanyrak["address"],
    #                 "area": shanyrak["area"],
    #                 "rooms_count": shanyrak["rooms_count"],
    #                 "description": shanyrak["description"],
    #             }
    #         },
    #     )
    
    def update_comment(self, shanyrak_id: str, comment_id: str, new_content: str):
        query = {"_id": ObjectId(shanyrak_id), "comments._id": ObjectId(comment_id)}
        update = {"$set": {"comments.$.comment": new_content}}
        self.database["shanyraks"].update_one(query, update)
        
    def delete_comment(self, shanyrak_id: str, comment_id: str):
        self.database["shanyraks"].update_one(
            {"_id": ObjectId(shanyrak_id)},
            {"$pull": {"comments": {"_id": ObjectId(comment_id)}}}
        )
    
        
        

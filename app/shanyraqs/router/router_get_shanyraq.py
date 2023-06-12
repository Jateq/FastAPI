from typing import Any

from fastapi import Depends
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class GetMyShanyraqResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str
    user_id: str

@router.get("/shanyraks/{id}")
def get_element_by_id(id: str):
    try:
        document = collection.find_one({'_id': ObjectId(id)})
        if document:
            return document
        else:
            raise HTTPException(status_code=404, detail="Element not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server error")

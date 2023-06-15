from fastapi import APIRouter, Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router
from typing import Any
from pydantic import Field


class CreateShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str  
    
class CreateShanyrakResponse(AppModel):
    id: Any = Field(alias="_id")
    

@router.post("/", response_model=CreateShanyrakResponse)
def create_new_shanyrak(
    input: CreateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    payload = input.dict()
    payload["user_id"] = jwt_data.user_id
    shanyrak_id = svc.repository.create_shanyrak(payload)
    return CreateShanyrakResponse(id=shanyrak_id)
    # return Response(status_code=200)

from fastapi import Depends, HTTPException, status
from typing import Any
from app.utils import AppModel
from pydantic import Field
from ..service import Service, get_service
from . import router

from ..adapters.jwt_service import JWTData
from .dependencies import parse_jwt_user_data


class CreateShanyraqRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateShanyraqResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateShanyraqResponse,
)
def create_shanyraq(
    input: CreateShanyraqRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    user = svc.repository.create_shanyraq(jwt_data.user_id, input.dict())

    return CreateShanyraqResponse(email=input.email)

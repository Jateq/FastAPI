from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router

class PatchMyShanyrakRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str 
    


@router.patch("/{shanyrak_id:str}")
def update_my_ashanyrak(
    shanyrak_id: str,
    input: PatchMyShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    payload = input.dict()
    updated_shanyrak = svc.repository.update_shanyrak(shanyrak_id, jwt_data.user_id, payload)
    return Response(status_code=200)

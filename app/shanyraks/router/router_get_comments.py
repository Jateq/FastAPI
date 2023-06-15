from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router
 
class GetMyShanyrakResponse(AppModel):
    comments: Any 


@router.get("/{id}/comments", response_model=GetMyShanyrakResponse)
def get_comments(
    shanyrak_id: str,
    svc: Service = Depends(get_service),
) -> GetMyShanyrakResponse:
    shanyrak_comments = svc.repository.get_comments(shanyrak_id)
    return GetMyShanyrakResponse(comments=shanyrak_comments)
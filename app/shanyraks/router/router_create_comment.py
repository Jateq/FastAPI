from fastapi import APIRouter, Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router
from typing import Any
from pydantic import Field

import datetime


class CreateCommentRequest(AppModel):
    comment : str
    

@router.post("/{id}/comments")
def create_comment(
    shanyrak_id: str,
    input: CreateCommentRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    payload = input.dict()
    payload["created_at"] = datetime.datetime.now()
    payload["user_id"] = jwt_data.user_id
    svc.repository.create_comment(shanyrak_id, payload)
    return Response(status_code=200)
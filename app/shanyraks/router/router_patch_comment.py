from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router

class PatchMyShanyrakRequest(AppModel):
    comment: str
    


@router.patch("/{id}/comments/{comment_id}")
def update_my_comment(
    shanyrak_id: str,
    comment_id: str,
    input: PatchMyShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    new_comment = input.comment
    # payload = input.dict()
    # updated_shanyrak = svc.repository.update_shanyrak(shanyrak_id, jwt_data.user_id, payload)
    svc.repository.update_comment(shanyrak_id, comment_id, new_comment)
    return Response(status_code=200)
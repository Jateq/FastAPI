from typing import Any

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router


@router.delete("/{id}/comments/{comment_id}")
def delete_my_comment(
    shanyrak_id: str,
    comment_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.delete_comment(shanyrak_id, comment_id)
    return Response(status_code=200)
from typing import Any, List

from fastapi import Depends, Response
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service

from . import router

class DeleteMediaRequest(AppModel):
    media: List[Any]

@router.delete("/{id}/media")
def delete_media(
    input: DeleteMediaRequest,
    shanyrak_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.delete_media(shanyrak_id, jwt_data.user_id, input.media)
    return Response(status_code=200)
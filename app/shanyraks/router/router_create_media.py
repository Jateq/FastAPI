from fastapi import Depends, UploadFile, Response
from typing import List

from ..service import Service, get_service
from . import router

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

    
   
@router.post("/files")
def upload_files(
    shanyrak_id: str,
    files: List[UploadFile],
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
):
    result = []
    for file in files:
        url = svc.s3_service.upload_file(file.file, file.filename)
        result.append(url)
    svc.repository.create_media(shanyrak_id, jwt_data.user_id, result)
    return Response(status_code=200)
    
    
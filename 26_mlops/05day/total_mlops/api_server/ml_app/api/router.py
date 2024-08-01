from fastapi import APIRouter

from ml_app.api.endpoints import create_table, create_datas

api_router = APIRouter()
api_router.include_router(
    create_table.router, prefix="/learning-db", tags=["learning db"])
api_router.include_router(
    create_datas.router, prefix="/learning-db", tags=["learning db"])

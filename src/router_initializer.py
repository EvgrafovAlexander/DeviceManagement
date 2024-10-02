# thirdparty
from fastapi import APIRouter


def get_routers() -> list[APIRouter]:
    from src.management import router as device_router

    routers: list[APIRouter] = [
        device_router.router,
    ]
    return routers

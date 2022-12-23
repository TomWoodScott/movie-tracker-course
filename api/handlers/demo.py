from fastapi import APIRouter

demo_router = APIRouter(prefix="/api/v1/demo")


def hello_world():
    pass
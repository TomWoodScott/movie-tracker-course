from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from api.responses.detail import DetailResponse
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix="/api/v1/demo")

# GET - Retrieve data.
# POST - To send data.
# PUT, PATCH - To update data.
# DELETE - To delete data.

# it is important to keep endpoints stateless.
class NameIn(BaseModel):
    name: str
    prefix: str = "Mr"


@router.get("/", response_model=DetailResponse)
def hello_world():
    """
    This is the hello world end point
    """
    return DetailResponse(message="Hello World")


@router.get("/hello", response_model=DetailResponse)
def send_date_query(name: str = Query(..., title="User", description="The name")):
    return DetailResponse(message="Hello")


@router.post("/hello/name", response_model=DetailResponse)
def send_data_body(name: NameIn = Body(..., title="Body", description="This is some description")):
    """
    Response with Hello name, where name is user provided.
    """
    return DetailResponse(message=f"Hello, {name.prefix}. {name.name}")


@router.post("/hello/{name}", response_model=DetailResponse)
def send_data_body(name: str = Path(..., title="Name")):
    """
    Response with Hello name, where name is user provided.
    """
    return DetailResponse(message=f"Hello, {name}")


@router.delete(
    "/delete/{name}",
    response_model=DetailResponse,
    responses={404: {"model": DetailResponse}},
)
def delete_data(name: str):
    if name == "admin":
        raise JSONResponse(
            status_code=404,
            content=jsonable_encoder(
                DetailResponse(message="cannot delete data for admin")
            )
        )
    return DetailResponse(message=f"Data deleted for {name}")

# we choose not to use HTTPException as it gives us less adaptable error messages. 
# @router.delete(
#     "/error", response_model=DetailResponse, responses={404: {"model": DetailResponse}}
# )
# def get_error_http():
#     raise HTTPException(404, detail="This endpoint always fails.") 

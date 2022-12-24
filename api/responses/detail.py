from pydantic import BaseModel


class DetailResponse(BaseModel):
    response: str

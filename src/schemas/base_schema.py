from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Any

class BaseSchema(BaseModel):
    

    class Config:
        from_attributes = True
        frozen = True


T = TypeVar(name="Schemas", bound=Any)


class ResponseSchema(BaseSchema, Generic[T]):
    """
    Base schema for all responses.
    """

    status: str = Field(..., description="Status of the response")
    message: str = Field(..., description="Message of the response")
    data: T = Field(..., description="Data of the response")
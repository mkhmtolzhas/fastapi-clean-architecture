from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    

    class Config:
        from_attributes = True
from typing import Type, TypeVar
from pydantic import BaseModel
from src.models.base_model import BaseModel as SQLAlchemyModel  


T = TypeVar("T", bound=SQLAlchemyModel)
S = TypeVar("S", bound=BaseModel)


def model_to_schema(model: SQLAlchemyModel, schema_type: Type[S]) -> S:
    """
    Преобразование модели в схему.
    """
    return schema_type.model_validate(model, from_attributes=True)

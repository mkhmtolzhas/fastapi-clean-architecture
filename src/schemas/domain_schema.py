from pydantic import Field
from .base_schema import BaseSchema

class DomainCreateSchema(BaseSchema):
    """
    Schema for creating a domain.
    """
    name: str = Field(..., description="Domain name")
    description: str = Field(..., description="Domain description")
    is_active: bool = Field(default=True, description="Is the domain active?")

class DomainUpdateSchema(DomainCreateSchema):
    """
    Schema for updating a domain.
    """
    id: int = Field(..., description="Domain ID")


class DomainReadSchema(DomainUpdateSchema):
    """
    Schema for reading a domain.
    """
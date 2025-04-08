from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class DomainModel(BaseModel):
    __tablename__ = "domains"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
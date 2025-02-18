from typing import Optional
from sqlmodel import Field, SQLModel

class Button(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=True, primary_key=True)
    effect_type: str
    effect_dir: str
    name: str
    color: str
    icon: str
    page: int
    code: str = Field(unique=True)
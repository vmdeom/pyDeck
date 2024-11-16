from typing import Optional
from sqlmodel import Field, SQLModel

class Button(SQLLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=True, primary_key=True)
    effect_type: str
    efect_dir: str
    name: str
    code: str = Field(unique=True)

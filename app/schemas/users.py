from typing import Any, Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name: str


class UserDelete(BaseModel):
    id: int


class UserResponse(BaseModel):
    id: int
    name: str
    state: Optional[str] = None
    data: Optional[dict[str, Any]] = None

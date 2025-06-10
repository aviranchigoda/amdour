from typing import Optional
from sqlmodel import SQLModel, Field


class Tenant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password_hash: str
    tenant_id: int | None = Field(default=None, foreign_key="tenant.id")
    is_admin: bool = False

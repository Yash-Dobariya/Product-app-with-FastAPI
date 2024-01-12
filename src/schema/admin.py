from pydantic import BaseModel
from typing import Optional


class CreateAdmin(BaseModel):
    username: str
    email: str
    password: str
    mobile_no: str


class ResponseAdmin(BaseModel):
    """give admin response"""

    id: str
    username: str
    email: str
    mobile_no: str

    class Config:
        orm_mode = True


class AdminLogin(BaseModel):
    """check login validation"""

    username: str
    password: str


class PermissionRequest(BaseModel):
    permission: bool


class AdminUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    mobile_no: Optional[str] = None

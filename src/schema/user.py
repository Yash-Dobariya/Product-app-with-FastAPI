from pydantic import BaseModel, EmailStr
from typing import Optional


class Request_User(BaseModel):
    """check validation of user info"""

    full_name : str
    username : str
    password : str
    email : EmailStr
    mobile_no : str
    address : str

class Response_User(BaseModel):
    """check validation of response user info"""

    id: str
    full_name : str
    username : str
    email : EmailStr
    mobile_no : str
    address : str

    class Config:
        orm_mode = True


class Login(BaseModel):
    """check login validation"""

    username: str
    password: str


class Update_User(BaseModel):
    """check validation of update user info"""

    full_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile_no: Optional[str] = None
    address: Optional[str] = None

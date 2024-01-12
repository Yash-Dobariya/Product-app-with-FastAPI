from pydantic import BaseModel
from typing import Optional


class CreateProduct(BaseModel):
    name: str
    price: int
    description: str
    stock: int


class ResponseProduct(BaseModel):
    id: str
    name: str
    price: int
    description: str
    stock: int

class UpdateProduct(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    stock: Optional[int] = None

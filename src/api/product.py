from fastapi import Depends, APIRouter
from src.services.product import ProductService
from src.schema.product import CreateProduct, ResponseProduct, UpdateProduct
from sqlalchemy.orm import Session
from src.database import get_db
from src.utils.jwt_token import get_current_user
from typing import List


product_route = APIRouter()
PRODUCT = ProductService()


@product_route.post("/create_product", response_model=ResponseProduct)
def create_product(
    product_data: CreateProduct,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """create product API"""
    return PRODUCT.create_product_service(db, product_data, current_user)


@product_route.get("/product/{product_id}", response_model=ResponseProduct)
def get_user_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """get user particular product API"""
    return PRODUCT.get_product_service(db, product_id)


@product_route.get("/user/{user_id}/products", response_model=List[ResponseProduct])
def get_user_all_product(
    user_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """get particular user all products API"""

    return PRODUCT.get_user_all_product_service(db, user_id)


@product_route.put("/product/{product_id}")
def update_product(
    product_id: str,
    product_data: UpdateProduct,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """update product API"""

    return PRODUCT.update_product_service(db, product_id, product_data, current_user)


@product_route.delete("/product/{product_id}")
def delete_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),  
):
    """delete product API"""

    return PRODUCT.delete_product_service(db, product_id, current_user)

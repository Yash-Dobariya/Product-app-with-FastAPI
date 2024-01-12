from fastapi import APIRouter, Depends
from src.schema.admin import (
    CreateAdmin,
    ResponseAdmin,
    AdminLogin,
    PermissionRequest,
    AdminUpdate,
)
from src.database import get_db
from sqlalchemy.orm import Session
from src.utils.jwt_token import get_current_user
from src.services.admin import AdminService
from src.schema.user import Response_User
from typing import List


admin_route = APIRouter()
ADMIN = AdminService()


@admin_route.post("/create_admin", response_model=ResponseAdmin)
def create_admins(admin_data: CreateAdmin, db: Session = Depends(get_db)):
    """Create admin"""

    return ADMIN.create_admin_service(db, admin_data)


@admin_route.post("/admin_login")
def login(admin_data: AdminLogin, db: Session = Depends(get_db)):
    """create admin API"""

    return ADMIN.admin_login_service(db, admin_data)


@admin_route.get("/user_requests", response_model=List[Response_User])
def user_requests(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    """get all user requests API"""

    return ADMIN.user_requests_service(db)


@admin_route.post("/give_permission/{user_id}")
def request_permission(
    user_id: str,
    permission: PermissionRequest,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """admin can approve and decline of user permission API"""

    return ADMIN.give_requests_permission_service(db, user_id, permission.permission)


@admin_route.get("/all_admin", response_model=List[ResponseAdmin])
def all_admins(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """get all admins API"""

    return ADMIN.all_admin_services(db)


@admin_route.put("/update_admin/{admin_id}")
def update_admin(
    admin_id: str,
    admin_data: AdminUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """update admin API"""

    return ADMIN.update_admin_services(db, admin_id, admin_data, current_user)


@admin_route.delete("/delete_admin/{admin_id}")
def delete_admin(
    admin_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """delete admin API"""

    return ADMIN.delete_admin_service(db, admin_id, current_user)

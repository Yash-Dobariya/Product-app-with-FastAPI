from fastapi import APIRouter
from src.schema.user import Request_User, Response_User, Login, Update_User
from src.services.user import UserService
from sqlalchemy.orm import Session
from src.database import get_db
from fastapi import Depends
from src.utils.jwt_token import get_current_user
from typing import List


user_route = APIRouter()
USER = UserService()


@user_route.post("/signup")
def sign_up(user_data: Request_User, db: Session = Depends(get_db)):
    """user signup API"""

    return USER.signup_service(db, user_data)


@user_route.post("/login")
def login(user_data: Login, db: Session = Depends(get_db)):
    """login user API"""

    return USER.login_service(db, user_data)


@user_route.get("/get_user/{user_id}", response_model=Response_User)
def get_particular_user(
    user_id,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """get particular user"""

    return USER.get_user_service(db, user_id)


@user_route.get("/all_users", response_model=List[Response_User])
def get_all_user(
    db: Session = Depends(get_db), current_user: str = Depends(get_current_user)
):
    """get all users"""

    return USER.get_all_users_services(db)


@user_route.put("/update_user/{user_id}")
def update_user(
    user_id: str,
    user_data: Update_User,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """update user"""

    return USER.update_user_service(db, user_id, user_data)

@user_route.delete("/delete_user/{user_id}")
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    """delete user"""

    return USER.delete_user_service(db, user_id)

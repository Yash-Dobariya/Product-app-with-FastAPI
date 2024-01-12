from src.model.user import User
from src.utils.jwt_token import access_token, refresh_token
from fastapi import HTTPException, status
from datetime import datetime


class UserService:
    """User services"""

    def signup_service(self, db, user_data):
        """signup service"""

        user = User(**user_data.dict())
        db.add(user)
        db.commit()

        return {"message": "Successfully send a request to admin for approval"}

    def login_service(self, db, user_data):
        """logic service"""

        user = (
            db.query(User)
            .filter(
                User.username == user_data.username,
                User.password == user_data.password,
                User.is_deleted == False,
            )
            .first()
        )

        if user:
            if user.is_approved == False or user.is_approved == None:
                return {"message": "Your request is pending, wait for admin approval"}
            elif user.is_approved == True:
                access = access_token(
                    {"id": user.id, "email_id": user.email}
                )
                refresh = refresh_token(
                    {"id": user.id, "email_id": user.email}
                )

                return {"access_token": access, "refresh_token": refresh}

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid username and email",
            )

    def get_user_service(self, db, user_id):
        """get particular user service"""

        user = (
            db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        )

        return user

    def get_all_users_services(self, db):
        """get all users service"""

        user = db.query(User).filter(User.is_deleted == False).all()

        return user

    def update_user_service(self, db, user_id, user_data):
        """update user service"""

        user = (
            db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        )

        for field, value in user_data.dict(exclude_unset=True).items():
            setattr(user, field, value)

        user.updated_at = datetime.utcnow()
        db.commit()
        return {"message": f"Successfully {user_id} updated"}

    def delete_user_service(self, db, user_id):
        """delete user service"""

        user = (
            db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        )

        user.deleted_at = datetime.utcnow()
        user.is_deleted = True
        db.commit()
        return {"message": f"Successfully {user} deleted"}

from src.model.admin import Admin
from src.utils.jwt_token import access_token, refresh_token
from src.model.user import User
from datetime import datetime


class AdminService:
    """all admin services"""

    def create_admin_service(self, db, admin_data):
        """create admin service"""

        admin = Admin(**admin_data.dict())
        db.add(admin)
        db.commit()

        return admin

    def admin_login_service(self, db, admin_data):
        """login service for admin"""

        admin = (
            db.query(Admin)
            .filter(
                Admin.username == admin_data.username,
                Admin.password == admin_data.password,
                Admin.is_deleted == False,
            )
            .first()
        )

        if admin:
            access = access_token({"id": admin.id, "email": admin.email})
            refresh = refresh_token({"id": admin.id, "email": admin.email})

            return {"access_token": access, "refresh_token": refresh}
        else:
            {"message": "your username and password wrong"}

    def user_requests_service(self, db):
        """get all user pending requests"""

        users = (
            db.query(User)
            .filter(User.is_approved == False, User.is_deleted == False)
            .all()
        )

        return users

    def give_requests_permission_service(self, db, user_id, permission):
        """give user requests permission service"""

        user = (
            db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
        )

        user.is_approved = permission
        db.commit()

        return {"message": f"given {permission} permission of {user_id}"}

    def all_admin_services(self, db):
        """get all admin services"""

        admins = db.query(Admin).filter(Admin.is_deleted == False).all()
        return admins

    def update_admin_services(self, db, admin_id, admin_data, current_user):
        """update admin service"""

        admin = (
            db.query(Admin)
            .filter(Admin.id == admin_id, Admin.is_deleted == False)
            .first()
        )

        for field, value in admin_data.dict(exclude_unset=True).items():
            setattr(admin, field, value)

        admin.updated_at = datetime.utcnow()
        admin.updated_by = current_user
        db.commit()

        return {"message": f"Successfully updated {admin_id}"}
    
    def delete_admin_service(self, db, admin_id, current_user):
        """delete admin service"""

        admin = (
            db.query(Admin)
            .filter(Admin.id == admin_id, Admin.is_deleted == False)
            .first()
        )

        admin.is_deleted = True
        admin.deleted_at = datetime.utcnow()
        admin.deleted_by = current_user
        db.commit()

        return {"message": f"Successfully deleted {admin_id}"}

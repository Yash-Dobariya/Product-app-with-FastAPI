import jwt
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.model.user import User
from src.model.admin import Admin


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def access_token(subject: dict):
    """create access token"""

    expire = datetime.utcnow() + timedelta(days=1)
    subject = {"exp": expire, **subject}
    token = jwt.encode(payload=subject, key=SECRET_KEY, algorithm=ALGORITHM)

    return token


def refresh_token(subject: dict):
    """create refresh token"""

    expire = datetime.utcnow() + timedelta(days=7)
    subject = {"exp": expire, **subject}
    token = jwt.encode(payload=subject, key=SECRET_KEY, algorithm=ALGORITHM)

    return token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        user = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        try:
            db.query(User).filter(
                User.id == user.get("id"),
                User.email == user.get("email_id"),
                User.is_deleted == False,
            ).first()
            return user.get("id")
        except:
            db.query(Admin).filter(
                Admin.id == user.get("id"),
                Admin.email == user.get("email_id"),
                Admin.is_deleted == False,
            ).first()

            return user.get("id")

    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Token Expired"
        )

    except jwt.exceptions.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid token"
        )

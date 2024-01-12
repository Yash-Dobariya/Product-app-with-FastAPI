from src.database import Base
from src.utils.same_model import DBmodel
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class User(Base, DBmodel):
    """user table"""

    __tablename__ = "user"

    full_name = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    mobile_no = Column(String)
    address = Column(String)
    role = Column(String, default="USER")
    is_approved = Column(Boolean, default=False)

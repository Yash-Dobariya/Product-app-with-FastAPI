from src.database import Base
from src.utils.same_model import DBmodel
from sqlalchemy import Column, String


class Admin(Base, DBmodel):
    """admin table"""

    __tablename__ = "admin"

    username = Column(String)
    email = Column(String)
    password = Column(String)
    mobile_no = Column(String)
    role = Column(String, default="ADMIN")

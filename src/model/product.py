from src.database import Base
from src.utils.same_model import DBmodel
from sqlalchemy import Column, String, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.model.user import User


class Product(Base, DBmodel):
    """Product table"""

    __tablename__ = "product"

    name = Column(String)
    price = Column(BigInteger)
    description = Column(String)
    stock = Column(Integer)
    user_id = Column(String, ForeignKey(User.id))

    _user_ = relationship("User", foreign_keys=[user_id])

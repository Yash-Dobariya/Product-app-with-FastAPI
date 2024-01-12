from uuid import uuid4
from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime


def default_uuid():
    return str(uuid4())


class DBmodel:
    """same model entity"""

    id = Column(String, default=default_uuid, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime)
    updated_by = Column(String)
    deleted_at = Column(DateTime)
    deleted_by = Column(String)
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

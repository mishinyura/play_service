from app.models.base_model import BaseModel
from sqlalchemy import Column, String
from app.core.db import Base
from app.models.base_model import BaseModel


class User(BaseModel, Base):
    __tablename__ = 'users'

    message = Column(String, index=True)
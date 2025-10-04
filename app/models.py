from sqlalchemy import Column, Integer, String, Uuid
from app.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


class Transfer(Base):
    __tablename__ = "transfer"
    id = Column(Uuid, nullable=False)
    valor = Column(String, nullable=False)




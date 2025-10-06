from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class Transfer(Base):
    __tablename__ = "transfer"
    id = Column(Integer, nullable=False, primary_key=True)
    sender_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    receiver_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    uuid = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)
    valor = Column(String, nullable=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])





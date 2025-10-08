from sqlalchemy import Column, Integer, String, UUID, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from app.database import Base
import uuid
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Transfer(Base):
    __tablename__ = "transfer"
    id = Column(Integer, nullable=False, primary_key=True)
    sender_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    uuid = Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4)
    valor = Column(Numeric(10, 2), nullable=False)
    time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])





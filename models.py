from sqlalchemy import Column, DateTime, Integer, String, func

from database import Base


class NameEntry(Base):
    __tablename__ = "name_entries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

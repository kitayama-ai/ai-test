from sqlalchemy import Column, Integer, String, DateTime, Text
from .database import Base
from datetime import datetime

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    user_message = Column(Text)
    ai_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)
    status = Column(String, default="replied") # replied, pending, error

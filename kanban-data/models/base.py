from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    user_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.created_at = datetime.utcnow

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
        }

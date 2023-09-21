from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, user_id):
        self.user_id = user_id

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
        }

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from .base import BaseModel

class Priority(BaseModel):
    __tablename__ = 'priority'
    
    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String(40), nullable=False)
    color = Column(String(20), nullable=False)
    
    tasks = relationship("Task", back_populates="priority", lazy="joined")

    def __init__(self, name, color, user_id):
        self.name = name
        self.color = color
        super().__init__(user_id)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
        }

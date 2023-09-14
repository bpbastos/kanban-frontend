from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from .base import BaseModel

class Board(BaseModel):
    __tablename__ = 'board'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)

    workflows = relationship("Workflow", back_populates="board", lazy="joined")

    def __init__(self, name, user_id):
        self.name = name
        super().__init__(user_id)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from models.base import BaseModel
from models.board import Board



class Workflow(BaseModel):
    __tablename__ = 'workflow'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    color = Column(String(20), nullable=False)
    name = Column(String(40), nullable=False)
    board_id = Column(GUID, ForeignKey(Board.id), nullable=False)

    board = relationship("Board", back_populates="workflows", lazy="joined")
    tasks = relationship("Task", back_populates="workflow", cascade="all, delete-orphan", lazy="joined")

    def __init__(self, color, name, board_id):
        self.color = color
        self.name = name
        self.board_id = board_id

    def to_dict(self):
        return {
            'id': self.id,
            'color': self.color,
            'name': self.name
        }
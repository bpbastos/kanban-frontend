from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import BaseModel
from models.board import Board

class Workflow(BaseModel):
    __tablename__ = 'workflow'

    id = Column(Integer, primary_key=True, autoincrement=True)
    color = Column(String)
    name = Column(String)
    board_id = Column(Integer, ForeignKey(Board.id), nullable=False)

    board = relationship("Board", back_populates="workflows", lazy="joined")
    tasks = relationship("Task", back_populates="workflow", lazy="joined")

    def __init__(self, color, name, board_id, user_id):
        self.color = color
        self.name = name
        self.board_id = board_id
        super().__init__(user_id)

    def to_dict(self):
        return {
            'id': self.id,
            'color': self.color,
            'name': self.name
        }
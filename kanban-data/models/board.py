from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import BaseModel

class Board(BaseModel):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True, autoincrement=True)
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

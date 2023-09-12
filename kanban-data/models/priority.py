from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Priority(Base):
    __tablename__ = 'priorities'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="priority", lazy="joined")

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
        }

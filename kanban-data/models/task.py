from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import BaseModel
from models.priority import Priority
from models.workflow import Workflow

class Task(BaseModel):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    totalSubTasks = Column(Integer, nullable=False, default=0)
    totalSubTasksDone = Column(Integer, nullable=False, default=0)
    
    priority_id = Column(Integer, ForeignKey(Priority.id), nullable=False)
    workflow_id = Column(Integer, ForeignKey(Workflow.id), nullable=False)    

    priority = relationship("Priority", back_populates="tasks", lazy="joined")
    workflow = relationship("Workflow", back_populates="tasks", lazy="joined")
    subtasks = relationship("SubTask", back_populates="task", lazy="joined")

    def __init__(self, title, totalSubTasks, totalSubTasksDone, user_id):
        self.title = title
        self.totalSubTasks = totalSubTasks
        self.totalSubTasksDone = totalSubTasksDone
        super().__init__(user_id)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'totalSubTasks': self.totalSubTasks,
            'totalSubTasksDone': self.totalSubTasksDone,
            'priority': self.priority.to_dict(),
            'subtasks': [subtask.to_dict() for subtask in self.subtasks]
        }
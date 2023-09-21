from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

from models.base import BaseModel
from models.priority import Priority
from models.workflow import Workflow

class Task(BaseModel):
    __tablename__ = 'task'

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    title = Column(String(40), nullable=False)
    description = Column(String(4000), nullable=False, default="")    
    total_sub_tasks = Column(Integer, nullable=False, default=0)
    total_sub_tasks_done = Column(Integer, nullable=False, default=0)
    
    priority_id = Column(GUID, ForeignKey(Priority.id), nullable=False)
    workflow_id = Column(GUID, ForeignKey(Workflow.id), nullable=False)    

    workflow = relationship("Workflow", back_populates="tasks", lazy="joined")
    priority = relationship("Priority", back_populates="tasks", lazy="joined")
    subtasks = relationship("SubTask", back_populates="task", cascade="all, delete-orphan", lazy="joined", order_by="SubTask.created_at")

    def __init__(self, title, description, priority_id, workflow_id):
        self.title = title
        self.description = description
        self.priority_id = priority_id
        self.workflow_id = workflow_id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'total_sub_tasks': self.total_sub_tasks,
            'total_sub_tasks_done': self.total_sub_tasks_done,
            'priority': self.priority.to_dict(),
            'subtasks': [subtask.to_dict() for subtask in self.subtasks]
        }
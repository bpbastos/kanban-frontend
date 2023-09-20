from typing import TYPE_CHECKING, Annotated, List

import strawberry

from models.task import Task as TaskModel

#Circular depency hell
if TYPE_CHECKING:
    from .workflow import Workflow
    from .subtask import SubTask
    from .priority import Priority

@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    description: str    
    total_sub_tasks: int
    total_sub_tasks_done: int
    priority: Annotated["Priority", strawberry.lazy(".priority")]
    workflow: Annotated["Workflow", strawberry.lazy(".workflow")]
    subtasks: List[Annotated["SubTask", strawberry.lazy(".subtask")]]

    @classmethod
    def marshal(cls, model: TaskModel) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            description=model.description,
            total_sub_tasks=model.total_sub_tasks,
            total_sub_tasks_done=model.total_sub_tasks_done,
            priority=model.priority,
            workflow=model.workflow,
            subtasks=model.subtasks
        )
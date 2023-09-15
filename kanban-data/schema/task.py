from typing import TYPE_CHECKING, Annotated, List

import strawberry

from models.task import Task as TaskModel

from .priority import Priority

from .subtask import SubTask
#Circular depency hell
if TYPE_CHECKING:
    from .workflow import Workflow

@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    total_sub_tasks: int
    total_sub_tasks_done: int
    priority: Priority
    workflow: Annotated["Workflow", strawberry.lazy(".workflow")]
    subtasks: List[SubTask]

    @classmethod
    def marshal(cls, model: TaskModel) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            total_sub_tasks=model.total_sub_tasks,
            total_sub_tasks_done=model.total_sub_tasks_done,
            priority=Priority.marshal(model.priority) if model.priority else None,
            workflow=Workflow.marshal(model.workflow) if model.workflow else None,
            subtasks=[SubTask.marshal(st) for st in model.subtasks] if model.subtasks else []
        )
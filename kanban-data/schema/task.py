import strawberry

from models.task import Task as TaskModel
from models.subtask import SubTask as SubTaskModel
from models.priority import Priority as PriorityModel

from .priority import Priority
from .subtask import SubTask

@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    total_sub_tasks: int
    total_sub_tasks_done: int
    priority: Priority
    subtasks: list[SubTask]

    @classmethod
    def marshal(cls, model: TaskModel) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            total_sub_tasks=model.total_sub_tasks,
            total_sub_tasks_done=model.total_sub_tasks_done,
            priority=PriorityModel.marshal(model.priority) if model.priority else None,
            subtasks=[SubTaskModel.marshal(st) for st in model.subtasks] if model.subtasks else []
        )
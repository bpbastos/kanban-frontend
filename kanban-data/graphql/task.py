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
    priority: PriorityModel
    subtasks: list[SubTaskModel]

    @classmethod
    def marshal(cls, model: TaskModel) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            total_sub_tasks=model.totalSubTasks,
            total_sub_tasks_done=model.totalSubTasksDone,
            priority=Priority.marshal(model.priority) if model.priority else None,
            subtasks=[SubTask.marshal(st) for st in model.subtasks] if model.subtasks else []
        )
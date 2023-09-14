import strawberry

from .task import Task as Task

@strawberry.type
class Workflow:
    id: strawberry.ID
    color: str
    name: str
    tasks: list[Task]
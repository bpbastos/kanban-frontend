import strawberry

from models.workflow import Workflow as WorkflowModel
from .task import Task

@strawberry.type
class Workflow:
    id: strawberry.ID
    color: str
    name: str
    tasks: list[Task]
    @classmethod
    def marshal(cls, model: WorkflowModel) -> "Workflow":
        return cls(
            id=strawberry.ID(str(model.id)),
            color=model.color,
            name=model.name,
            tasks=[Task.marshal(t) for t in model.tasks] if model.tasks else []
        )    
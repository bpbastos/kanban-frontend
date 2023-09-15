from typing import TYPE_CHECKING, Annotated, List

import strawberry

from models.workflow import Workflow as WorkflowModel

from .task import Task

#Circular depency hell
if TYPE_CHECKING:
    from schema.board import Board

@strawberry.type
class Workflow:
    id: strawberry.ID
    color: str
    name: str
    board: Annotated["Board", strawberry.lazy(".board")]
    tasks: List[Task]

    @classmethod
    def marshal(cls, model: WorkflowModel) -> "Workflow":
        return cls(
            id=strawberry.ID(str(model.id)),
            color=model.color,
            name=model.name,
            board=model.board,
            tasks=model.tasks
        )    
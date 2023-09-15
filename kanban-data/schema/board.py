from typing import TYPE_CHECKING, Annotated, List

import strawberry

from models.board import Board as BoardModel

#Circular dependency hell
if TYPE_CHECKING:
    from .workflow import Workflow

@strawberry.type
class Board:
    id: strawberry.ID
    name: str
    workflows: List[Annotated["Workflow", strawberry.lazy(".workflow")]]

    @classmethod
    def marshal(cls, model: BoardModel) -> "Board":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            workflows=model.workflows
        )
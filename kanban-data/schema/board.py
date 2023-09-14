import strawberry

from models.board import Board as BoardModel

from schema.workflow import Workflow

@strawberry.type
class Board:
    id: strawberry.ID
    name: str
    workflows: list[Workflow]

    @classmethod
    def marshal(cls, model: BoardModel) -> "Board":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            workflows=[Workflow.marshal(w) for w in model.workflows] if model.workflows else []
        )
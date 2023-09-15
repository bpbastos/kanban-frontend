from typing import TYPE_CHECKING, Annotated, List

import strawberry

from models.priority import Priority as PriorityModel

#Circular dependency hell
if TYPE_CHECKING:
    from .task import Task

@strawberry.type
class Priority:
    id: strawberry.ID
    name: str
    color: str
    tasks: List[Annotated["Task", strawberry.lazy(".task")]]

    @classmethod
    def marshal(cls, model: PriorityModel) -> "Priority":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            color=model.color,
            tasks=model.tasks
        )
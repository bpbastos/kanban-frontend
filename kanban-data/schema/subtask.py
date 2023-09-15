from typing import TYPE_CHECKING, Annotated

import strawberry

from models.subtask import SubTask as SubTaskModel

#Circular depency hell
if TYPE_CHECKING:
    from .task import Task

@strawberry.type
class SubTask:
    id: strawberry.ID
    title: str
    order: int
    done: bool
    task: Annotated["Task", strawberry.lazy(".task")]

    @classmethod
    def marshal(cls, model: SubTaskModel) -> "SubTask":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            order=model.order,
            done=model.done,
            task=model.task
        )
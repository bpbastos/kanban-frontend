import strawberry

from models.subtask import SubTask as SubTaskModel

@strawberry.type
class SubTask:
    id: strawberry.ID
    title: str
    order: int
    done: bool

    @classmethod
    def marshal(cls, model: SubTaskModel) -> "SubTask":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            order=model.order,
            done=model.done
        )
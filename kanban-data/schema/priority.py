import strawberry

from models.priority import Priority as PriorityModel

@strawberry.type
class Priority:
    id: strawberry.ID
    name: str
    color: str

    @classmethod
    def marshal(cls, model: PriorityModel) -> "Priority":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            color=model.color
        )
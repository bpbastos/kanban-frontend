import typing
import strawberry

# Definir os tipos de dados para as entidades
@strawberry.type
class Priority:
    id: strawberry.ID
    name: str
    color: str

@strawberry.type
class SubTask:
    id: strawberry.ID
    title: str
    order: int
    done: bool

@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    totalSubTasks: int
    totalSubTasksDone: int
    priority: Priority
    subtasks: list[SubTask]

@strawberry.type
class Workflow:
    id: strawberry.ID
    color: str
    name: str
    tasks: list[Task]

@strawberry.type
class Board:
    id: strawberry.ID
    name: str
    workflows: list[Workflow]
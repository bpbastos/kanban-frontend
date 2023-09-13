from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from fastapi import FastAPI
from typing import List
import strawberry

from sqlalchemy import select

import models

# Definir os tipos de dados para as entidades

@strawberry.type
class Priority:
    id: strawberry.ID
    name: str
    color: str
    @classmethod
    def marshal(cls, model: models.Priority) -> "Priority":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            color=model.color
        )


@strawberry.type
class SubTask:
    id: strawberry.ID
    title: str
    order: int
    done: bool

    @classmethod
    def marshal(cls, model: models.SubTask) -> "SubTask":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            order=model.order,
            done=model.done
        )    


@strawberry.type
class Task:
    id: strawberry.ID
    title: str
    totalSubTasks: int
    totalSubTasksDone: int
    priority: Priority
    subtasks: list[SubTask]

    @classmethod
    def marshal(cls, model: models.Task) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            totalSubTasks=model.totalSubTasks,
            totalSubTasksDone=model.totalSubTasksDone,
            priority=Priority.marshal(model.priority) if model.priority else None,
            subtasks=[SubTask.marshal(st) for st in model.subtasks] if model.subtasks else []
        )        


@strawberry.type
class Workflow:
    id: strawberry.ID
    color: str
    name: str
    tasks: list[Task]
    @classmethod
    def marshal(cls, model: models.Workflow) -> "Workflow":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            color=model.color,
            tasks=[Task.marshal(t) for t in model.tasks] if model.tasks else []
        )     


@strawberry.type
class Board:
    id: strawberry.ID
    name: str
    workflows: list[Workflow]
    @classmethod
    def marshal(cls, model: models.Board) -> "Board":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            workflows=[Workflow.marshal(w) for w in model.workflows] if model.workflows else []
        )       


@strawberry.type
class Query:
    @strawberry.field
    async def boards(self) -> list[Board]:
        async with models.get_session() as s:
            sql = select(models.Board)
            db_boards = (await s.execute(sql)).scalars().unique().all()
        return [Board.marshal(board) for board in db_boards]
    
    @strawberry.field
    async def board(self, info: Info, id: strawberry.ID) -> Board:
        async with models.get_session() as s:
            sql = select(models.Board).filter(models.Board.id == id)
            db_board = (await s.execute(sql)).scalars().unique().one()
        return Board.marshal(db_board) 


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

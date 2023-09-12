from strawberry.fastapi import GraphQLRouter
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

@strawberry.type
class Query:
    @strawberry.field
    async def board(self, info: Info, id: strawberry.ID) -> Board:
        db = models.get_session()
        board = db.query(Board).filter(Board.id == id).first()
        db.close()
        return board    
    

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
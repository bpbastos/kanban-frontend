from functools import cached_property
from strawberry.fastapi import GraphQLRouter, BaseContext 
from strawberry.types import Info as _Info
from strawberry.types.info import RootValueType
from fastapi import FastAPI
from httpx import AsyncClient
from datetime import datetime, timedelta
import strawberry
import os

from sqlalchemy import select

import models

"""
# Recupera as variaveis de ambiente (integração com kanban-usr-mgmt)
PARSE_SERVER_URL = os.getenv('PARSE_SERVER_URL')
PARSE_SERVER_APPID = os.getenv("PARSE_SERVER_APPID")
PARSE_SERVER_RESTAPIKEY = os.getenv("PARSE_SERVER_RESTAPIKEY")

@cached_property
async def get_user(token: str) -> User:
    async with AsyncClient(base_url=PARSE_SERVER_URL) as ac:
        headers = {
            "Content-Type": "application/json",
            "X-Parse-Application-Id": PARSE_SERVER_APPID,
            "X-Parse-REST-API-Key": PARSE_SERVER_RESTAPIKEY,
            "X-Parse-Session-Token": token
        }
        response = await ac.get("/users/me", headers=headers)
        if response.status_code == 200:
            rj = response.json()
            if rj.get("sessionToken") == token:
                dt = datetime.now()
                td = timedelta(hours=2)
                user = User()
                user.id = rj.get("objectId")
                user.username = rj.get("username")
                user.email = rj.get("email")
                user.token = rj.get("token")
                return user
        return None
"""

class Context(BaseContext):
    @cached_property
    def user(self) -> dict | None:
        if not self.request:
            return None
        user_id = self.request.headers.get("User-Id", None)
        return {"id": user_id}


Info = _Info[Context, RootValueType]


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
    total_sub_tasks: int
    total_sub_tasks_done: int
    priority: Priority
    subtasks: list[SubTask]

    @classmethod
    def marshal(cls, model: models.Task) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            title=model.title,
            total_sub_tasks=model.totalSubTasks,
            total_sub_tasks_done=model.totalSubTasksDone,
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


@strawberry.input
class WorkflowInput:
    color: str
    name: str

@strawberry.input
class AddBoardInput:
    name: str
    workflows: list[WorkflowInput]



@strawberry.type
class Query:
    @strawberry.field()
    async def boards(self, info: Info) -> list[Board]:
        user_id = info.context.user.get('id')
        async with models.get_session() as s:
            sql = select(models.Board).filter(models.Board.user_id == user_id)
            db_boards = (await s.execute(sql)).scalars().unique().all() | []
        return [Board.marshal(board) for board in db_boards]

    @strawberry.field()
    async def board(self, info: Info, id: strawberry.ID) -> Board:
        user_id = info.context.user.get('id')
        async with models.get_session() as s:
            sql = select(models.Board).filter(models.Board.id == id).filter(models.Board.user_id == user_id)
            db_board = (await s.execute(sql)).scalars().unique().one()
        return Board.marshal(db_board)
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_board(self, info: Info, board: AddBoardInput) -> Board:
        async with models.get_session() as s:
            newBoard = models.Board(name=board.name,user_id=info.context.user.get('id'))
            s.add(newBoard)
            await s.flush()
            for w in board.workflows:
                newWorkflow = models.Workflow(name=w.name,color=w.color,board_id=newBoard.id,user_id=info.context.user.get('id'))
                s.add(newWorkflow)
            await s.commit() 
        return Board.marshal(newBoard)
    

async def get_context() -> Context:
    return Context()

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

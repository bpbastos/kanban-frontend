
from typing import List, Optional
from sqlalchemy import select
import strawberry

from .board import Board
from .priority import Priority
from .task import Task

from . import Info
from . import UserNotFound

from models.board import Board as BoardModel
from models.priority import Priority as PriorityModel
from models.task import Task as TaskModel
from models import get_session

@strawberry.type
class Query:
    @strawberry.field()
    async def boards(self, info: Info) -> List[Board]:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(BoardModel).filter(BoardModel.user_id == user_id).order_by(BoardModel.created_at.desc())
            db_boards = (await s.execute(sql)).scalars().unique().all()
        return [Board.marshal(board) for board in db_boards]

    @strawberry.field()
    async def priorities(self, info: Info) -> List[Priority]:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(PriorityModel).order_by(PriorityModel.created_at.desc())
            db_priorities = (await s.execute(sql)).scalars().unique().all()
        return [Priority.marshal(priority) for priority in db_priorities]    

    @strawberry.field()
    async def board(self, info: Info, id: Optional[strawberry.ID] = None) -> Board:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(BoardModel).filter(BoardModel.user_id == user_id)\
                                        .order_by(BoardModel.created_at.desc())
            if id:
                sql = select(BoardModel).filter(BoardModel.id == id) \
                                        .filter(BoardModel.user_id == user_id)
                
            db_board = (await s.execute(sql)).scalars().first()

        return Board.marshal(db_board)

    @strawberry.field()
    async def task(self, info: Info, id: strawberry.ID) -> Task:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(TaskModel).filter(TaskModel.id == id).filter(TaskModel.user_id == user_id).order_by(TaskModel.created_at.desc())
            db_task = (await s.execute(sql)).scalars().first()
        return Task.marshal(db_task)      
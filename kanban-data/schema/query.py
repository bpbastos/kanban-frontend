
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
class BoardNotFoundResponse(): 
    message: str = "Quadro não encontrado"

@strawberry.type
class PriorityNotFoundResponse(): 
    message: str = "Prioridade não encontrada"    

@strawberry.type
class TaskNotFoundResponse(): 
    message: str = "Tarefa não encontrada"       

SearchBoardResponse = strawberry.union("BoardResponse", (Board, BoardNotFoundResponse, UserNotFound))    

SearchPriorityResponse = strawberry.union("PriorityResponse", (Priority, PriorityNotFoundResponse, UserNotFound))    

SearchTaskResponse = strawberry.union("TaskResponse", (Task, TaskNotFoundResponse, UserNotFound))    

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

            #if not db_boards:
            #    return BoardNotFoundResponse()              
            
        return [Board.marshal(board) for board in db_boards]

    @strawberry.field()
    async def priorities(self, info: Info) -> List[Priority]:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(PriorityModel).order_by(PriorityModel.created_at.desc())
            db_priorities = (await s.execute(sql)).scalars().unique().all()

            #if not db_priorities:
            #    return PriorityNotFoundResponse()
            
        return [Priority.marshal(priority) for priority in db_priorities]    

    @strawberry.field()
    async def board(self, info: Info, id: Optional[strawberry.ID] = None) -> SearchBoardResponse:
        user_id = info.context.user.get('id')
        if not user_id:
            return UserNotFound()
        
        async with get_session() as s:
            sql = select(BoardModel).filter(BoardModel.user_id == user_id)\
                                        .order_by(BoardModel.created_at.desc())
            if id:
                sql = select(BoardModel).filter(BoardModel.id == id) \
                                        .filter(BoardModel.user_id == user_id)
                
            db_board = (await s.execute(sql)).scalars().first()

            if not db_board:
                return BoardNotFoundResponse()                

        return Board.marshal(db_board)

    @strawberry.field()
    async def task(self, info: Info, id: strawberry.ID) -> SearchTaskResponse:
        user_id = info.context.user.get('id')
        if not user_id:
            return UserNotFound()
        
        async with get_session() as s:
            sql = select(TaskModel).filter(TaskModel.id == id).order_by(TaskModel.created_at.desc())
            db_task = (await s.execute(sql)).scalars().first()

            if not db_task:
                return TaskNotFoundResponse()

        return Task.marshal(db_task)      
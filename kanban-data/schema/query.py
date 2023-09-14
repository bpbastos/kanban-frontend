
from sqlalchemy import select
import strawberry

from .board import Board
from . import Info
from . import UserNotFound

from models.board import Board as BoardModel
from models import get_session

@strawberry.type
class Query:
    @strawberry.field()
    async def boards(self, info: Info) -> list[Board]:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(BoardModel).filter(BoardModel.user_id == user_id)
            db_boards = (await s.execute(sql)).scalars().unique().all()
        return [Board.marshal(board) for board in db_boards]

    @strawberry.field()
    async def board(self, info: Info, id: strawberry.ID) -> Board:
        user_id = info.context.user.get('id')
        #if not user_id:
        #    return UserNotFound()
        
        async with get_session() as s:
            sql = select(BoardModel).filter(BoardModel.id == id).filter(BoardModel.user_id == user_id)
            db_board = (await s.execute(sql)).scalars().unique().one_or_none()
        return Board.marshal(db_board)
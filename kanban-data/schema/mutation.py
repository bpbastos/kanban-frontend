from models.board import Board as BoardModel
from models.workflow import Workflow as WorkflowModel
from models.priority import Priority as PriorityModel
from models import get_session

from schema.board import Board
from schema.priority import Priority
from . import Info

import strawberry

@strawberry.input
class PriorityInput:
    color: str
    name: str

@strawberry.input
class WorkflowInput:
    color: str
    name: str

@strawberry.input
class AddBoardInput:
    name: str
    workflows: list[WorkflowInput]

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_board(self, info: Info, board: AddBoardInput) -> Board:
        async with get_session() as s:
            newBoard = BoardModel(name=board.name,user_id=info.context.user.get('id'))
            s.add(newBoard)
            await s.flush()
            for w in board.workflows:
                newWorkflow = WorkflowModel(name=w.name,color=w.color,board_id=newBoard.id,user_id=info.context.user.get('id'))
                s.add(newWorkflow)
            await s.commit() 
        return Board.marshal(newBoard)
    
    @strawberry.mutation
    async def add_priority(self, info: Info, priority: PriorityInput) -> Priority:
        async with get_session() as s:
            newPriority = PriorityModel(name=priority.name,color=priority.color,user_id=info.context.user.get('id'))
            s.add(newPriority)
            await s.commit() 
        return Priority.marshal(newPriority)    
    

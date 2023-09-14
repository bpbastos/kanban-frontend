from models.board import Board as BoardModel
from models.workflow import Workflow as WorkflowModel
from models.priority import Priority as PriorityModel
from models.task import Task as TaskModel
from models import get_session

from schema.board import Board
from schema.priority import Priority
from schema.task import Task
from . import Info

from sqlalchemy import select
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
class AddBoardResponse:    
    id: strawberry.ID

@strawberry.type
class AddPriorityResponse:    
    id: strawberry.ID

@strawberry.type
class AddTaskResponse:    
    id: strawberry.ID


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_board(self, info: Info, board: AddBoardInput) -> AddBoardResponse:
        async with get_session() as s:
            new_board = BoardModel(name=board.name,user_id=info.context.user.get('id'))
            s.add(new_board)
            await s.flush()
            for w in board.workflows:
                newWorkflow = WorkflowModel(name=w.name,color=w.color,board_id=new_board.id,user_id=info.context.user.get('id'))
                s.add(newWorkflow)
            await s.commit() 
        return AddBoardResponse(id=new_board.id)
    
    @strawberry.mutation
    async def add_priority(self, info: Info, priority: PriorityInput) -> AddPriorityResponse:
        async with get_session() as s:
            new_priority = PriorityModel(name=priority.name,color=priority.color,user_id=info.context.user.get('id'))
            s.add(new_priority)
            await s.flush()
            await s.commit() 
        return AddPriorityResponse(id=new_priority.id)  

    @strawberry.mutation
    async def add_task(self, info: Info, title:str, workflow_id: strawberry.ID) -> AddTaskResponse:
        async with get_session() as s:
            sql = select(PriorityModel).filter(PriorityModel.name == "Baixa")
            db_priority = (await s.execute(sql)).scalars().unique().one_or_none()
            new_task = TaskModel(title=title,priority_id=db_priority.id,workflow_id=workflow_id, user_id=info.context.user.get('id'))
            s.add(new_task)
            await s.flush()
            await s.commit() 
        return AddTaskResponse(id=new_task.id)

"""
mutation addNewTask ($title: String!, $boardId: ID!, $workflowId: ID!) {
	addTask(
    title: $title
    workflowId: $workflowId
    boardId: $boardId
  ) 
  {
    id
  }
}
"""    
    

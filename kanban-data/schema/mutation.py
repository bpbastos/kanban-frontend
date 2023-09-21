from models.board import Board as BoardModel
from models.workflow import Workflow as WorkflowModel
from models.priority import Priority as PriorityModel
from models.task import Task as TaskModel
from models.subtask import SubTask as SubTaskModel
from models import get_session

from . import Info
from . import UserNotFound

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
class BaseResponse:    
    pass    

@strawberry.type
class AddBoardSuccess(BaseResponse): 
    id: strawberry.ID

@strawberry.type
class AddPriorityResponse(BaseResponse):
    id: strawberry.ID

@strawberry.type
class AddPriorityResponse(BaseResponse):    
    id: strawberry.ID

@strawberry.type
class AddTaskResponse(BaseResponse):    
    id: strawberry.ID

@strawberry.type
class AddSubTaskResponse(BaseResponse):      
    id: strawberry.ID

@strawberry.type
class MarkSubTaskDoneResponse(BaseResponse):           
    id: strawberry.ID

@strawberry.type
class DeleteTaskResponse(BaseResponse):   
    id: strawberry.ID

@strawberry.type
class DeleteSubTaskResponse(BaseResponse): 
    id: strawberry.ID

@strawberry.type
class UpdateTaskResponse(BaseResponse):    
    id: strawberry.ID  


AddBoardResponse = strawberry.union("AddBoardResponse", (AddBoardSuccess, UserNotFound))   


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_board(self, info: Info, board: AddBoardInput) -> AddBoardResponse:
        user_id = info.context.user.get('id')
        if not user_id:
            return UserNotFound()
                
        async with get_session() as s:
            new_board = BoardModel(name=board.name,user_id=user_id)
            s.add(new_board)
            await s.flush()
            for w in board.workflows:
                newWorkflow = WorkflowModel(name=w.name,color=w.color,board_id=new_board.id)
                s.add(newWorkflow)
            await s.commit() 
        return AddBoardSuccess(id=new_board.id)
    
    @strawberry.mutation
    async def add_priority(self, info: Info, priority: PriorityInput) -> AddPriorityResponse:
        #user_id = info.context.user.get('id')
        async with get_session() as s:
            new_priority = PriorityModel(name=priority.name,color=priority.color)
            s.add(new_priority)
            await s.flush()
            await s.commit() 
        return AddPriorityResponse(id=new_priority.id)  

    @strawberry.mutation
    async def add_task(self, info: Info, title:str, workflow_id: strawberry.ID) -> AddTaskResponse:
        #user_id = info.context.user.get('id')
        async with get_session() as s:
            sql = select(PriorityModel).filter(PriorityModel.name == "Baixa")
            db_priority = (await s.execute(sql)).scalars().unique().one_or_none()
            new_task = TaskModel(title=title,description="",priority_id=db_priority.id,workflow_id=workflow_id)
            s.add(new_task)
            await s.flush()
            await s.commit() 
        return AddTaskResponse(id=new_task.id)

    @strawberry.mutation
    async def update_task(self, info: Info, id: strawberry.ID, title:str, description:str, priority_id: strawberry.ID) -> AddTaskResponse:
        #user_id = info.context.user.get('id')
        async with get_session() as s:
            sql = select(TaskModel).filter(TaskModel.id == id)
            db_task = (await s.execute(sql)).scalars().unique().one_or_none()
            if db_task:
                db_task.title = title
                db_task.description = description
                db_task.priority_id = priority_id
            await s.commit() 
        return UpdateTaskResponse(id=db_task.id)

    @strawberry.mutation
    async def delete_task(self, info: Info, task_id: strawberry.ID) -> DeleteTaskResponse:
        #user_id = info.context.user.get('id')
        async with get_session() as s:
            sql = select(TaskModel).filter(TaskModel.id == task_id)
            db_task = (await s.execute(sql)).scalars().unique().one_or_none()
            if db_task:
                await s.delete(db_task)
                await s.commit() 
        return DeleteTaskResponse(id=task_id)        
    
    @strawberry.mutation
    async def add_sub_task(self, info: Info, title:str, task_id: strawberry.ID) -> AddSubTaskResponse:
        #user_id = info.context.user.get('id')
        async with get_session() as s:
            sql = select(TaskModel).filter(TaskModel.id == task_id)
            db_task = (await s.execute(sql)).scalars().unique().one_or_none()
            if db_task:
                new_sub_task = SubTaskModel(title=title,order=0,done=False,task_id=task_id)
                s.add(new_sub_task)
                db_task.total_sub_tasks += 1
                await s.commit() 
        return AddSubTaskResponse(id=new_sub_task.id)   

    @strawberry.mutation
    async def mark_sub_task_done(self, info: Info, sub_task_id: strawberry.ID) -> MarkSubTaskDoneResponse:
        async with get_session() as s:
            sql = select(SubTaskModel).filter(SubTaskModel.id == sub_task_id)
            db_sub_task = (await s.execute(sql)).scalars().unique().one_or_none()
            if db_sub_task:
                sql = select(TaskModel).filter(TaskModel.id == db_sub_task.task_id)
                db_task = (await s.execute(sql)).scalars().unique().one_or_none()
                db_sub_task.done = not db_sub_task.done
                if db_sub_task.done:
                    db_task.total_sub_tasks_done += 1
                elif db_task.total_sub_tasks_done > 0:
                    db_task.total_sub_tasks_done -= 1
                await s.commit() 
        return MarkSubTaskDoneResponse(id=db_sub_task.id)   

    @strawberry.mutation
    async def delete_sub_task(self, info: Info, sub_task_id: strawberry.ID) -> DeleteSubTaskResponse:
        async with get_session() as s:
            sql = select(SubTaskModel).filter(SubTaskModel.id == sub_task_id)
            db_sub_task = (await s.execute(sql)).scalars().unique().one_or_none()
            if db_sub_task:
                sql = select(TaskModel).filter(TaskModel.id == db_sub_task.task_id)
                db_task = (await s.execute(sql)).scalars().unique().one_or_none()

                if db_sub_task.done and db_task.total_sub_tasks_done > 0:
                    db_task.total_sub_tasks_done -= 1
                    
                if db_task.total_sub_tasks > 0: 
                    db_task.total_sub_tasks -= 1   

                await s.delete(db_sub_task)       
                await s.commit() 
        return DeleteSubTaskResponse(id=db_sub_task.id)
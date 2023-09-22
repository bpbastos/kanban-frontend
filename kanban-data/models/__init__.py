from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
import asyncio
import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager
from typing import AsyncGenerator


# importando os elementos definidos no modelo
from models.base import Base
from models.board import Board
from models.priority import Priority
from models.subtask import SubTask
from models.task import Task
from models.workflow import Workflow

POSTGRES_HOST = os.environ.get('POSTGRES_HOST','localhost:5432')
POSTGRES_USER = os.environ.get('POSTGRES_USER','kanban')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD','kanbanpass')
POSTGRES_DB = os.environ.get('POSTGRES_DB','kanban')

# url de acesso ao banco (essa é uma url de acesso ao postgresql)
#postgresql+asyncpg://postgres:kanbandb@localhos:5432/kanban
DATABASE_URL = 'postgresql+asyncpg://%s:%s@%s/%s' % (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DB)

print (DATABASE_URL)

# cria a engine de conexão assíncrona com o banco
engine = create_async_engine(
    DATABASE_URL, 
    echo=True,
    future=True,
)

# Instancia um criador de seção com o banco
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()

async def _async_main():
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(
            insert(Priority), [
                {"name": "Baixa", "color":"info", "user_id":"none"},
                {"name": "Média", "color":"warning", "user_id":"none"},
                {"name": "Alta", "color":"error", "user_id":"none"},
            ]
        )
    await engine.dispose()
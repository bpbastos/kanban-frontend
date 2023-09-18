from functools import cached_property
from strawberry.fastapi import BaseContext 
from strawberry.types import Info as _Info
from strawberry.types.info import RootValueType
from httpx import AsyncClient

import strawberry
import os

"""
# Recupera as variaveis de ambiente (integração com kanban-usr-mgmt)
PARSE_SERVER_URL = os.getenv('PARSE_SERVER_URL')
PARSE_SERVER_APPID = os.getenv("PARSE_SERVER_APPID")
PARSE_SERVER_RESTAPIKEY = os.getenv("PARSE_SERVER_RESTAPIKEY")

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
        user_id = self.request.headers.get("X-User-Id", None)
        return {"id": user_id}


Info = _Info[Context, RootValueType]

async def get_context() -> Context:
    return Context()

@strawberry.type
class UserNotFound:
    message: str = "Usuário não encontrado"
    code: str = "210"

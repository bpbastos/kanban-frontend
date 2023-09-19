from strawberry.fastapi import GraphQLRouter 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry

from schema.query import Query
from schema.mutation import Mutation
from schema import get_context

import os

FRONTEND_URL = os.getenv('FRONTEND_URL')

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()

origins = [
    FRONTEND_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(graphql_app, prefix="/graphql")

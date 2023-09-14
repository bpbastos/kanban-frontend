from strawberry.fastapi import GraphQLRouter 
from fastapi import FastAPI
import strawberry

from schema.query import Query
from schema.mutation import Mutation
from schema import get_context

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

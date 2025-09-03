from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from internal.db import postgres
from internal.schemas.user import UserResponse, UserRequest
from internal import crud



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with postgres.engine.begin() as conn:
        await conn.run_sync(postgres.Base.metadata.create_all())
    yield
    await postgres.engine.dispose()


app = FastAPI(lifespan=lifespan)    


@app.get("/users/", response_model=list[UserResponse])
async def create_user(session: AsyncSession = Depends(postgres.get_db)):
    return await crud.get_users(session)

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserRequest, session: AsyncSession = Depends(postgres.get_db)):
    return await crud.create_user(session, user)

@app.get
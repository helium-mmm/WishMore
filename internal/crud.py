from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from internal.model import model
from internal.schemas import user 

async def create_user(db: AsyncSession, new_user: model.UserRequest):
    db_user = model.User(email=new_user.email, name=new_user.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession):
    result = await db.execute(select(model.User))
    return result.scalars().all()
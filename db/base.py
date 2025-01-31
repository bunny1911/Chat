# coding=utf-8

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from local_conf import *


DATABASE_URL = f"postgresql+asyncpg://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


engine = create_async_engine(DATABASE_URL, echo=True)


Base = declarative_base()


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

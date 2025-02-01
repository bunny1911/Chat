# coding=utf-8

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from conf import DB

# Defined DB url
DATABASE_URL = f"postgresql+asyncpg://{DB['login']}:{DB['password']}@{DB['host']}/{DB['name']}"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

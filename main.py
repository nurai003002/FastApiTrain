from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title='Tranding app'
)

fastapi_users = FastAPIUsers[User,int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.base_config import auth_backend, fastapi_users, google_oauth_client
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from database import User
from test.router import router_test


app = FastAPI(title="Auth microservice")

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

app.include_router(router_test)

app.include_router(
    fastapi_users.get_oauth_router(google_oauth_client, auth_backend, "SECRET"),
    prefix="/auth/google",
    tags=["auth"],
)
from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users, google_oauth_client
from auth.schemas import UserRead, UserCreate
from breakdowns_log.router import router as router_breakdowns_log

app = FastAPI(title="Breakdown log service")

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

app.include_router(
    fastapi_users.get_oauth_router(google_oauth_client, auth_backend, "SECRET"),
    prefix="/auth/google",
    tags=["auth"],
)

app.include_router(router_breakdowns_log)

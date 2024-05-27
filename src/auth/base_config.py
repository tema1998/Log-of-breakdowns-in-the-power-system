from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from auth.manager import get_user_manager
from config import GOOGLE_CLIENT, GOOGLE_SECRET
from database import User
from httpx_oauth.clients.google import GoogleOAuth2

cookie_transport = CookieTransport(cookie_name="temas_cookies", cookie_max_age=3600)

SECRET = "SECRET"

google_oauth_client = GoogleOAuth2(GOOGLE_CLIENT, GOOGLE_SECRET)



def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
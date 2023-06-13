from config import endpoints

from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse

from ninja import Router

from config.constants.api_const import HttpStatus
from src.common.schemas.common_schemas import ResponseSchema
from src.security.schemas import CredentialSchema, JWTTokenSchema, RefreshTokenSchema
from src.security.services.jwt_service import AuthBearer
from src.security.services.login_service import LoginPageService
from src.security.services.logout_service import LogoutService
from src.security.services.refresh_token_service import RefreshTokenService
from src.account.schemas import UserInfoSchema


auth_router = Router(tags=['security'])
User = get_user_model()
"""
# depends on the database data
{
  "email": "test@test.com",
  "password": "Test2021#"
}
"""


@auth_router.post("/login", response={
    HttpStatus.OK.value: JWTTokenSchema,
    HttpStatus.BAD_REQUEST.value: ResponseSchema,
    HttpStatus.UNAUTHORIZED.value: ResponseSchema,
},
                  url_name=endpoints.SECURITY_LOGIN_URL)
def login(request: HttpRequest, payload: CredentialSchema) -> tuple:
    """login function"""
    return LoginPageService(request, payload).execute()


@auth_router.post("/refresh_token", response={
    HttpStatus.OK.value: JWTTokenSchema,
    HttpStatus.BAD_REQUEST.value: ResponseSchema,
    HttpStatus.UNAUTHORIZED.value: ResponseSchema,
},
                  url_name=endpoints.SECURITY_REFRESH_TOKEN_URL)
def refresh_token(request: HttpRequest, payload: RefreshTokenSchema) -> tuple:
    """
    This method expects the refresh token is valid.
    If the refresh token is valid, a new pair is generated (access and refresh tokens)
    """
    return RefreshTokenService(request, payload).execute()


@auth_router.post("/logout", response={
    HttpStatus.OK.value: ResponseSchema,
    HttpStatus.UNAUTHORIZED.value: ResponseSchema,
}, auth=AuthBearer(),
                  url_name=endpoints.SECURITY_LOGOUT_URL)
def logout(request: HttpRequest) -> tuple:
    """Logout method"""
    return LogoutService(request).logout()


@auth_router.get("/user", response={200: UserInfoSchema, 403: ResponseSchema}, auth=AuthBearer(),
                 url_name=endpoints.SECURITY_USER_URL)
def get_auth_user_detail(request: HttpRequest):
    try:
        user = User.objects.get(id=request.auth.id)
        return 200, UserInfoSchema(first_name=user.first_name, last_name=user.last_name, email=user.email,
                                   permissions=list(user.get_all_permissions()))
    except (Exception,):
        return 403, ResponseSchema(detail="Authorization error")

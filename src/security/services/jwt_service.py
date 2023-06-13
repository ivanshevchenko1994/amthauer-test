from django.contrib.auth import get_user_model
from django.http import HttpRequest

from ninja.security import HttpBearer

from config.constants.api_const import ErrorResponse, ErrorKeys, HttpStatus
from src.common.schemas.common_schemas import ResponseSchema
from src.security.models import RefreshToken
from src.security.repositories import JWTTokenRepository
from src.security.schemas import JWTTokenSchema, TokenAuthSchema
from src.security.utils import JWTTokenManager
from django.shortcuts import get_object_or_404

User = get_user_model()


class JWTTokenBaseService:
    __slots__ = 'jwt_token_manager', 'request'

    def __init__(self, request: HttpRequest):
        self.jwt_token_manager = JWTTokenManager()
        self.request = request

    def update_token(self, class_instance: User | RefreshToken | None) -> tuple:

        if class_instance is not None:
            if isinstance(class_instance, RefreshToken):
                jwt_token = self.jwt_token_manager.create_jwt_token(class_instance.user_id)
            elif isinstance(class_instance, User):
                jwt_token = self.jwt_token_manager.create_jwt_token(class_instance.id)
            else:
                return HttpStatus.UNAUTHORIZED.value, {
                    ErrorKeys.MESSAGE.value: ErrorResponse.INVALID_REFRESH_TOKEN.value
                }
            # Check and delete old refresh_token if token exists
            # JWTTokenRepository.delete_refresh_token(jwt_token['user_id'])
            # Create new refresh token
            JWTTokenRepository.create_refresh_token(jwt_token['user_id'], jwt_token['refresh_token'],
                                                    self.jwt_token_manager.generate_refresh_token_lifetime())
            return HttpStatus.OK.value, JWTTokenSchema(**jwt_token)
        return HttpStatus.UNAUTHORIZED.value, ResponseSchema(**{
            ErrorKeys.MESSAGE.value: ErrorResponse.INVALID_CREDENTIALS.value
        })


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: str) -> get_user_model:
        jwt_payload = JWTTokenManager.check_jwt_token_if_valid_return_user_id(token)
        if jwt_payload is not None:
            try:
                token_data = TokenAuthSchema(**jwt_payload)
            except Exception as e:
                return None
            # return UserRepository.get_user_by_id_or_404(token_data.user_id)
            return get_object_or_404(User, id=token_data.user_id)

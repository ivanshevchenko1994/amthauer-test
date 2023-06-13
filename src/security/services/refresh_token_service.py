from config.constants import api_const
from django.http import HttpRequest

from src.security.repositories import JWTTokenRepository
from src.security.schemas import RefreshTokenSchema
from src.security.services.jwt_service import JWTTokenBaseService


class RefreshTokenService(JWTTokenBaseService):
    __slots__ = 'request', 'payload'

    def __init__(self, request: HttpRequest, payload: RefreshTokenSchema):
        super().__init__(request)
        self.payload = payload

    def execute(self) -> tuple:
        token = JWTTokenRepository.is_refresh_token_exists_and_valid(self.payload.refresh_token)
        if token is None:
            return api_const.HttpStatus.UNAUTHORIZED.value, {
                api_const.ErrorKeys.MESSAGE.value: api_const.ErrorResponse.INVALID_REFRESH_TOKEN.value
            }
        return self.update_token(token)

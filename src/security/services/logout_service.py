from config.constants import api_const

from src.security.repositories import JWTTokenRepository
from src.security.services.jwt_service import JWTTokenBaseService


class LogoutService(JWTTokenBaseService):
    __slots__ = 'request'

    def __init__(self, request):
        super().__init__(request)

    def logout(self) -> tuple:
        refresh_token = JWTTokenRepository.get_refresh_token_by_user_id(self.request.auth.id)

        if refresh_token is not None:
            JWTTokenRepository.delete_refresh_token(self.request.auth.id)
        return 200, {"detail": 'Delete refresh token from DB and logout user'}

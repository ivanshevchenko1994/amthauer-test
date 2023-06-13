from django.contrib.auth import authenticate

from src.security.schemas import CredentialSchema
from src.security.services.jwt_service import JWTTokenBaseService


class LoginPageService(JWTTokenBaseService):
    __slots__ = 'request', 'payload'

    def __init__(self, request, payload: CredentialSchema):
        super().__init__(request)
        self.payload = payload

    def _authenticate_user_by_username_password(self):
        return authenticate(self.request, username=self.payload.email, password=self.payload.password)

    def execute(self) -> tuple:
        user = self._authenticate_user_by_username_password()
        return self.update_token(user)

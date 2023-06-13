from datetime import datetime

from src.security.models import RefreshToken


class JWTTokenRepository:

    @staticmethod
    def get_refresh_token_by_user_id(user_id: int) -> RefreshToken | None:
        return RefreshToken.objects.filter(user_id=user_id).first()

    @staticmethod
    def is_refresh_token_exists_and_valid(refresh_token: str) -> RefreshToken | None:
        return RefreshToken.objects.filter(refresh_token=refresh_token, expires_at__gte=datetime.utcnow(),
                                           is_valid=True).first()

    @staticmethod
    def has_user_refresh_token(user_id: int) -> bool:
        token = RefreshToken.objects.filter(user_id=user_id).first()
        if token is not None:
            return True
        return False

    @staticmethod
    def delete_refresh_token(user_id: int) -> None:
        if JWTTokenRepository.has_user_refresh_token(user_id):
            RefreshToken.objects.filter(user_id=user_id).delete()

    @staticmethod
    def create_refresh_token(user_id: int, refresh_token: str, expires_at: datetime,
                             is_valid: bool = True) -> RefreshToken:
        return RefreshToken.objects.create(
            user_id=user_id,
            refresh_token=refresh_token,
            is_valid=is_valid,
            expires_at=expires_at
        )

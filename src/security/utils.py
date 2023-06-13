import jwt
from jwt import PyJWTError

from datetime import datetime, timedelta

from config import settings
from config.constants import api_const


class JWTTokenManager:

    @staticmethod
    def generate_access_token_lifetime():
        return datetime.utcnow() + timedelta(minutes=api_const.ACCESS_TOKEN_LIFETIME_MINUTES)

    @staticmethod
    def generate_refresh_token_lifetime():
        return datetime.utcnow() + timedelta(days=api_const.REFRESH_TOKEN_LIFETIME_DAYS)

    # class JWTTokenService:
    def create_jwt_access_token(self, user_id: int) -> str:
        jwt_payload = {
            "exp": self.generate_access_token_lifetime(),
            "sub": api_const.ACCESS_TOKEN_SUB,
            "user_id": user_id,
        }
        print(jwt_payload)
        encoded_jwt = jwt.encode(jwt_payload, settings.SECRET_KEY, algorithm=api_const.JWT_ALGORITHM)
        return encoded_jwt

    def create_jwt_refresh_token(self, user_id: int) -> str:
        jwt_payload = {
            "exp": self.generate_refresh_token_lifetime(),
            "sub": api_const.REFRESH_TOKEN_SUB,
            "user_id": user_id,
        }
        print(jwt_payload)
        encoded_jwt = jwt.encode(jwt_payload, settings.SECRET_KEY, algorithm=api_const.JWT_ALGORITHM)
        return encoded_jwt

    def create_jwt_token(self, user_id: int) -> dict:
        jwt_token = {
            "user_id": user_id,
            "access_token": self.create_jwt_access_token(user_id),
            "refresh_token": self.create_jwt_refresh_token(user_id),
            "token_type": api_const.TOKEN_TYPE,
        }
        return jwt_token

    @staticmethod
    def check_jwt_token_if_valid_return_user_id(token: str) -> dict | None:
        print(settings.SECRET_KEY)
        try:
            jwt_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[api_const.JWT_ALGORITHM])
            if jwt_payload['sub'] == api_const.REFRESH_TOKEN_SUB:
                return None
            return jwt_payload
        except jwt.exceptions.ExpiredSignatureError as e:
            print(e)
            return None
        except PyJWTError as e:
            print(e)
            return None

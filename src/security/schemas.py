from ninja import Schema, ModelSchema


class CredentialSchema(Schema):
    email: str
    password: str


class Token(Schema):
    id: int
    access_token: str
    token_type: str


class JWTTokenSchema(Schema):
    user_id: int
    access_token: str
    refresh_token: str
    token_type: str


class TokenAuthSchema(Schema):
    user_id: int
    exp: str
    sub: str


class RefreshTokenSchema(Schema):
    refresh_token: str

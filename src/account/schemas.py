from ninja import Schema, Field


class UserInfoSchema(Schema):
    email: str | None
    first_name: str | None
    last_name: str | None
    permissions: list[str] | None = Field(default=list())

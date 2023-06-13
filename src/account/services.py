from django.db.models import QuerySet

from src.account.models import User
from src.account.value_objects import UserId


def get_user_instance_by_user_id(user_id: UserId) -> User | QuerySet:
    return User.objects.get(id=user_id)

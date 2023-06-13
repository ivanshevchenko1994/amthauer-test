from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class RefreshToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    refresh_token = models.TextField()
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'refresh_token'

    def __str__(self) -> str:
        return f'{self.refresh_token}'

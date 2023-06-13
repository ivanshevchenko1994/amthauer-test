from django.contrib import admin

from src.security.models import RefreshToken


@admin.register(RefreshToken)
class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_valid', "created_at", "expires_at", 'refresh_token')
    search_fields = ('user__email', 'refresh_token')
    ordering = ('id',)

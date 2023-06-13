from django.contrib import admin

from src.account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "get_full_name", "is_active", "created_at")
    search_fields = ("id", "email", "first_name", "last_name")
    list_filter = ("is_active", )
    ordering = ("id", )

    def save_model(self, request, obj, form, change):
        # Generate a hashed password if the password field is provided
        if 'password' in form.changed_data and form.cleaned_data['password']:
            obj.set_password(form.cleaned_data['password'])

        super().save_model(request, obj, form, change)

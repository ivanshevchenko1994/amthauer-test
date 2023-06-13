from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.common.mixins.models.date_time_mixin import DateTimeMixin


class UserManager(BaseUserManager):

    def create_superuser(self, email: str, first_name: str, last_name: str,
                         password: str, **extra_fields: dict[str, any]) -> "User":
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        return self.create_user(email, first_name, last_name, password, **extra_fields)

    def create_user(self, email: str, first_name: str, last_name: str, password: str, **extra_fields: dict) -> "User":
        if not email:
            raise ValueError(_('Users must have an email'))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )

        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixin):
    email = models.EmailField(verbose_name=_('Email'), unique=True, max_length=255,
                              db_index=True)  # Email
    first_name = models.CharField(verbose_name=_('First name'), max_length=255,
                                  null=True, db_index=True)  # First name
    last_name = models.CharField(verbose_name=_('Last name'), max_length=255,
                                 null=True, db_index=True)  # Last name
    password = models.CharField(_('Password'), max_length=128)  # password
    is_admin = models.BooleanField(default=False)  # default status Django
    is_superuser = models.BooleanField(default=False)  # default status Django
    is_staff = models.BooleanField(default=False)  # default status Django
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.',
        ),
    )  # default status Django

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    class Meta:
        managed = True
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

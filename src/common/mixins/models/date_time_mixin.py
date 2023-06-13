from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

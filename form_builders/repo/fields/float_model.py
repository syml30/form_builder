from django.db import models
from form_builders.models import AnswerModel


class Float(models.Model):
    value = models.FloatField(
        blank=False,
        null=False,
    )
    answer = models.ForeignKey(
        to=AnswerModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    required = models.BooleanField(default=False)
    help_text = models.TextField(
        blank=True,
        null=True,
    )

    place_holder = models.CharField(
        max_length=215,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        blank=False,
        null=False,
    )
    extra_attribute = models.JSONField()

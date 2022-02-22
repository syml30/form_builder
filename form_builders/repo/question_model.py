from django.db import models
from form_builders.models import FormModel


class Question(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    number = models.IntegerField()
    form = models.ForeignKey(
        to=FormModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

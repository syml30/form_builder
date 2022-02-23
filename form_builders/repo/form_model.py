from django.db import models
from form_builders.models import FormGroupModel


class Form(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    group = models.ForeignKey(
        to=FormGroupModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.title}-{self.group}"

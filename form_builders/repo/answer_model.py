from django.db import models
from form_builders.models import AnswerTypModel


class Answer(models.Model):
    typ = models.ForeignKey(
        to=AnswerTypModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False,

    )

    def __str__(self):
        return str(self.typ)

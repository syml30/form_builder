from django.db import models


class AnswerTyp(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.title)

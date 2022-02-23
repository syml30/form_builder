from django.db import models


class FormGroup(models.Model):
    title = models.CharField(
        max_length=500,
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.title)

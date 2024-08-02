from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Visit(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def clean(self):
        if not self.description:
            raise ValidationError('This field is required.')

    def __str__(self):
        return f"Visit(date={self.date}, description={self.description})"

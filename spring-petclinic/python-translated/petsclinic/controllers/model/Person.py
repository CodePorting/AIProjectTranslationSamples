from django.db import models
from django.core.exceptions import ValidationError

class Person(BaseEntity):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def clean(self):
        if not self.first_name:
            raise ValidationError({'first_name': 'This field is required.'})
        if not self.last_name:
            raise ValidationError({'last_name': 'This field is required.'})

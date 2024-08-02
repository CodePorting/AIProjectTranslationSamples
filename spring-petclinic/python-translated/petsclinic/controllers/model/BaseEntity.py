from django.db import models

class BaseEntity(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

    def is_new(self):
        return self.id is None

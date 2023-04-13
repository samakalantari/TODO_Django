from django.db import models

# Create your models here.
class BaseModel(models.Model):
    creation_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    is_deleted = models.DateTimeField()

    class Meta:
        abstract = True  # Set this model as Abstract

class Task(BaseModel):

    title = models.CharField()
    description = models.TextField()
    is_done = models.BooleanField()

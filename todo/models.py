from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    is_important = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length=75)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description

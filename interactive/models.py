
from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    result = models.CharField(max_length=40)     # "minor" or "adult"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.age}) -> {self.result}"

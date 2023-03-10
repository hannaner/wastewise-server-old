from django.db import models
from django.contrib.auth import get_user_model

class Spot(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Spot: {self.title} / Description: {self.description}"
    
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Deferrable, UniqueConstraint

class User(AbstractUser):
    pass

class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_reviews")
    word = models.CharField(max_length = 25)
    definition = models.CharField(max_length = 280)
    times = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','word'],name='user_word'
            )
        ]

    def __str__(self):
        return f"{self.user} needs to review {self.word}"

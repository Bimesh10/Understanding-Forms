from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=100)
    rating = models.IntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.rating}"

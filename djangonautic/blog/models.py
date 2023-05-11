from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.TextField()

    def __str__(self):
        return self.title

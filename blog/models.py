from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateField()
    updated_on = models.DateField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

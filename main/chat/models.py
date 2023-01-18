from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)
    words = models.TextField(null=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.words


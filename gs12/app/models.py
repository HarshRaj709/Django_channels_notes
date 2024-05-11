from django.db import models

class Chat(models.Model):
    content = models.CharField(max_length=2000)
    time = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group',on_delete=models.CASCADE)

class Group(models.Model):
    group = models.CharField(max_length=150)

    def __str__(self):
        return self.group







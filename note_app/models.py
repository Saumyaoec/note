from django.db import models

class Note(models.Model):
    noteId = models.CharField(max_length=36, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

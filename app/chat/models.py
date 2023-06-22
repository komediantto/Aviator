from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.ForeignKey('Room',
                             on_delete=models.CASCADE,
                             related_name='messages')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class Room(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

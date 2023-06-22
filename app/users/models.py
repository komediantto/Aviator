from django.contrib.auth import get_user_model
from django.db import models
from chat.models import Room

User = get_user_model()


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, max_length=160,
                             null=True, blank=True,
                             on_delete=models.DO_NOTHING)
    balance = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            room = Room.objects.create(
                name=self.user.username + '_chat',
                url=f'/chat/{self.user.username}_chat/')
            self.room = room
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

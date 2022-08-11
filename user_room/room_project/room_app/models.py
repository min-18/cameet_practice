from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=5)
    age = models.IntegerField(default=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return str(self.id) + ". "+ self.name


class Room(models.Model):
    user_id = models.ForeignKey(User, related_name='rooms',on_delete=models.CASCADE,null=True)
    # user_id = models.ManyToManyField(User, verbose_name='유저')
    room_title = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.room_title}"
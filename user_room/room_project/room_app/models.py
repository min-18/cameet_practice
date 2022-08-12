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
    user_key = models.ForeignKey(User, related_name='rooms',on_delete=models.CASCADE,null=True)
    # user_id = models.ManyToManyField(User, verbose_name='유저')
    room_title = models.CharField(max_length=20)
    room_interest = models.CharField(max_length=20)
    room_place =  models.CharField(max_length=50)
    room_date = models.DateField(auto_now_add=True)
    room_time = models.TimeField(auto_now_add=True)
    room_headcount = models.IntegerField(default=1)
    room_status = models.IntegerField(default=0)
    room_created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_title}"
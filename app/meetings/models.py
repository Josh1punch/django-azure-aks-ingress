from django.db import models
from datetime import time
# Create your models here.
class Room(models.Model):
    roomName=models.CharField(max_length=200)
    flr=models.IntegerField(default=1)
    roomNum=models.IntegerField(default=12)
    def __str__(self):
       return  f"{self.roomName}: is on {self.flr} and number is {self.roomNum}"

class Meeting(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField()
    start_time=models.TimeField(default=time(9))
    duration=models.IntegerField(default=1)
    #link the room class when a meeting is created, and when a room is deleted all mtgs will be del on_delte==xxxx
    room=models.ForeignKey(Room,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

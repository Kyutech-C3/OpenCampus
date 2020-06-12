from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)

class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="None")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Comment(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()

class Game(models.Model):
    unityroom_url = models.CharField(max_length=255)

class Video(models.Model):
    url = models.CharField(max_length=255)

class Model3D(models.Model):
    sketchfab_id = models.CharField(max_length=255)

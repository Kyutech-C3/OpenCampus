from django.urls import reverse
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)

class Game(models.Model):
    unityroom_url = models.CharField(max_length=255)

class Video(models.Model):
    url = models.CharField(max_length=255)

class Model3D(models.Model):
    sketchfab_id = models.CharField(max_length=255)

class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="None")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
    model3d = models.ForeignKey(Model3D, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id),))

class Comment(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.work.id),))

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
    class WorkType(models.TextChoices):
        UNITY_3D = 'U3D', 'Unity 3D'
        UNITY_2D = 'U2D', 'Unity 2D'
        VIDEO = 'VID', 'VIDEO'
        MODEL_3D = 'M3D', 'MODEL 3D'
        OTHER = 'OTHER', 'OTHER'

    title = models.CharField(max_length=255)
    description = models.TextField(default="None")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    type_choice = models.TextField(choices=WorkType.choices, default=WorkType.OTHER)
    card_image = models.ImageField(null=False, upload_to='images/system/')

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

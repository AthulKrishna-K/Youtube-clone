from django.db import models

class youtube(models.Model):
    video = models.FileField(upload_to='videos/')  # New field for video upload
    description = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    views = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
  

    def __str__(self):
        return self.description

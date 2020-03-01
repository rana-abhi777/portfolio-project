from django.db import models

# Create your models here.
class Job(models.Model):
    # defining properties
    # Images - what it looks like
    image = models.ImageField(upload_to='images/')
    company = models.CharField(max_length=70)
    # summary
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.company
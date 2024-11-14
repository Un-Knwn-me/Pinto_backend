from django.db import models

# Cuisines:

class Cuisine(models.Model):
    title = models.CharField(max_length=255, unique=True)
    # image = models.ImageField(upload_to='foldername')

    def __str__(self):
        return self.title
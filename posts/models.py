from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    content= models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

from django.db import models

class Web(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='web/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

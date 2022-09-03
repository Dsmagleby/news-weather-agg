from django.db import models

class NewsField(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    image = models.URLField(null=True, blank=True)
    source = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    app_label = 'mainApp'
    
    def __str__(self):
            return self.titleS

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

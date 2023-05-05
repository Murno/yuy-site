from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField(upload_to=r'static\img\photo', height_field=None, width_field=None)


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name='Member'
        verbose_name_plural='Members'
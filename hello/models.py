from django.db import models

# Create your models here.

class Contact(models.Model):

    class Meta:
        app_label = "hello"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/', default='images/no-img.jpg')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
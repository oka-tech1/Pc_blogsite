from django.db import models

# Create your models here.
class pc_post(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='image/')
    ############################################
    proc = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    bat = models.CharField(max_length=255)
    drive = models.CharField(max_length=255)
    img1 = models.ImageField(upload_to='image/')
    img2 = models.ImageField(upload_to='image/')
    img3 = models.ImageField(upload_to='image/')
    comment = models.TextField(max_length=255)
    
    def __str__(self):
        return f'{self.name} {self.proc} {self.ram} {self.bat} {self.drive} {self.comment}'

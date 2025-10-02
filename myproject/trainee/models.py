from django.db import models

# Create your models here.
class Trainee(models.Model):
      id=models.AutoField(primary_key=True)
      name=models.CharField(max_length=100,null=False,default="")
      email=models.EmailField(unique=True)
      photo=models.ImageField(upload_to='trainee/images',null=True)


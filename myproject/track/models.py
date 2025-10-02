from django.db import models

# Create your models here.
#each class i create in model it becomes atable in database
#each variable in this class become acolumn in db
#each object become arow in db
#Model is the parent class that is responsible for creating atable in database
class track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)


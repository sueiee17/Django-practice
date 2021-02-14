from django.db import models

# Create your models here.


#class Role(models.Model):
 #   role=models.CharField(max_length=50)
    

class switchhost(models.Model):
    hostname=models.CharField(max_length=50)
    ipadd=models.CharField(max_length=50)
 #   devicerole= models.ForeignKey(Role, on_delete=models.CASCADE)

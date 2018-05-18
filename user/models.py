from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=11,verbose_name="电话")
    name_cn = models.CharField(max_length=30,null=True,blank=True)
    open_uid = models.CharField(max_length=10,null=True,)

    def __str__(self):
        return self.name_cn
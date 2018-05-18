from django.db import models

# Create your models here.
class Portal_app(models.Model):
    name = models.CharField(max_length=50, default="")
    portal_id = models.IntegerField()

    class Meta:
        verbose_name="入口应用"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Light_app(models.Model):
    app_type = models.IntegerField(default=1)
    catalog_id = models.IntegerField()
    mob_logo = models.CharField(max_length=200, default="")
    mob_url = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=50,)
    portal_id = models.ForeignKey(Portal_app,related_name="portalapp_lightapp")
    run_type = models.IntegerField(default=1)
    summary = models.CharField(max_length=100, null=True)

    author_id = models.ForeignKey('user.User',related_name='user_lightapps_author',null=True,)
    memberlist =models.ManyToManyField('user.User',related_name='user_lightapps_member')

    class Meta:
        verbose_name="轻应用"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
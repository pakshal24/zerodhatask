from django.db import models

# Create your models here.
class bhav(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.TextField()
    open = models.DecimalField(max_digits=10,decimal_places=2)
    high = models.DecimalField(max_digits=10,decimal_places=2)
    low = models.DecimalField(max_digits=10,decimal_places=2)
    close = models.DecimalField(max_digits=10,decimal_places=2)
    objects = models.Manager()



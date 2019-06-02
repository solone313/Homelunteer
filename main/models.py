from django.db import models

# Create your models here.
class Beneficiary(models.Model):
    address = models.CharField(max_length=200)
    vol_st = models.DateField()
    vol_en = models.DateField()
    sup_st = models.DateField()
    sup_en = models.DateField()
    people = models.IntegerField(default=0)
    status = models.BooleanField('모집 중', default=0)
    notice = models.BooleanField('긴급')
    image = models.ImageField(upload_to='home/images/', default="null")
    need = models.IntegerField()
    def __str__(self):
        return self.address

class Volunteer(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField()
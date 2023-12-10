from django.db import models

# Create your models here.

class Country(models.Model):
    cntr_name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.cntr_name

class Capital(models.Model):
    cap_name = models.CharField(max_length=100,primary_key=True)
    
    # cntr_name = models.ForeignKey(Country,on_delete=models.CASCADE,unique=True)
    
    cntr_name = models.OneToOneField(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.cap_name

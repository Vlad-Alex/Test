from django.db import models

# Create your models here.
class Worklist(models.Model):
    Name=models.CharField(max_length=250)
    Account=models.CharField(max_length=250)
    Country=models.CharField(max_length=250)

    def __str__(self):
        return self.Name + " - " + self.Country

class Ageing(models.Model):
    TotalAR=models.ForeignKey(Worklist, on_delete=models.CASCADE)
    Current=models.CharField(max_length=250)
    #Age60=models.CharField(max_length=250)

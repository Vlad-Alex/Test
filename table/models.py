from django.db import models

# Create your models here.
class financials_2015(models.Model):
    SAP_ID=models.CharField(max_length=250)
    entity_or_parent=models.CharField(max_length=250)
    Total_Assets=models.DecimalField(max_digits=10,decimal_places=0)

    def __str__(self):
        return self.SAP_ID + " - " + self.Total_Assets

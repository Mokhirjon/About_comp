from django.db import models

# Create your models here.
class Computers(models.Model):
    comp_name=models.CharField(default='',max_length=12)
    comp_vers=models.CharField(default='',max_length=49)
    comp_summa=models.CharField(default='',max_length=123456)
    date_of_created=models.DateField()
    other_info=models.CharField(default='',max_length=35433983730)

    def __str__(self):
        return self.comp_name
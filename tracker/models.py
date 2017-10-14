from django.db import models


# Create your models here.
class Transaction(models.Model):
    amount = models.IntegerField()
    category = models.CharField(max_length=200)
    section = models.CharField(max_length=200, blank=True)
    details = models.CharField(max_length=200, blank=True)
    date = models.DateField()

    def __str__(self):
        return 'Amount of %d in %s' % (self.amount, self.category)


# myapp/models.py

from django.db import models

class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.category}: ${self.amount} on {self.date}'

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    source = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.source}: ${self.amount} on {self.date}'

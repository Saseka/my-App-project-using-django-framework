# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Expense

@receiver(post_save, sender=Expense)
def handle_expense_save(sender, instance, created, **kwargs):
    if created:
        print(f'New expense added: {instance}')

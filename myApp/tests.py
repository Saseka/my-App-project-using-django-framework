from django.test import TestCase


# myapp/tests.py

from django.test import TestCase
from .models import Expense, Income

class ExpenseModelTest(TestCase):

    def setUp(self):
        Expense.objects.create(category="Food", amount=50.0, date="2024-07-24", description="Grocery shopping")
        Expense.objects.create(category="Transport", amount=20.0, date="2024-07-24", description="Bus ticket")

    def test_expense_creation(self):
        food_expense = Expense.objects.get(category="Food")
        transport_expense = Expense.objects.get(category="Transport")
        self.assertEqual(food_expense.amount, 50.0)
        self.assertEqual(transport_expense.amount, 20.0)
        self.assertEqual(str(food_expense), 'Food: $50.0 on 2024-07-24')
        self.assertEqual(str(transport_expense), 'Transport: $20.0 on 2024-07-24')

class IncomeModelTest(TestCase):

    def setUp(self):
        Income.objects.create(amount=1000.0, date="2024-07-24", source="Salary")

    def test_income_creation(self):
        income = Income.objects.get(source="Salary")
        self.assertEqual(income.amount, 1000.0)
        self.assertEqual(str(income), 'Salary: $1000.0 on 2024-07-24')

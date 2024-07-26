from django.shortcuts import render

# Create your views here.

# myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'expense_detail.html', {'expense': expense})

def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm()
    return render(request, 'expense_edit.html', {'form': form})

def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_edit.html', {'form': form})

from django.shortcuts import reverse, render, HttpResponseRedirect
from .models import Transaction
from .forms import TransactionForm


def index(request):
    transaction_list = Transaction.objects.all()
    category_totals = dict()
    for transaction in transaction_list:
        if transaction.category in category_totals:
            category_totals[transaction.category] += transaction.amount
        else:
            category_totals[transaction.category] = transaction.amount
    form = TransactionForm
    context = {
        'transaction_list': transaction_list,
        'category_totals': category_totals,
        'form': form,
    }
    return render(request, 'tracker/index.html', context)


def add_transaction(request):
    form = TransactionForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tracker:index'))

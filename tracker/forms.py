from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'amount': forms.TextInput(attrs={'size': '10'}),
            'date': forms.SelectDateWidget(),
        }

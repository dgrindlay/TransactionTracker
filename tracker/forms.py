from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'amount': forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
            'category': forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
            'section': forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
            'details': forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control', }),
        }

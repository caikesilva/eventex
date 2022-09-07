from django import forms
from django.core.exceptions import ValidationError

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 números', 'length')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=155)
    cpf = forms.CharField(label="CPF", max_length=14, validators=[validate_cpf])
    email = forms.EmailField(label="E-mail", required=False)
    phone = forms.CharField(label="Telefone", max_length=20, required=False)

    def clean_name(self):
        name = self.cleaned_data['name']

        return name.title()

    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        
        return self.cleaned_data
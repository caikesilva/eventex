from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=155)
    cpf = forms.CharField(label="CPF", max_length=11)
    email = forms.EmailField(label="E-mail")
    phone = forms.CharField(label="Telefone", max_length=20)
from django.db import models
from django.shortcuts import resolve_url as r
from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):
    name = models.CharField(max_length=155, verbose_name='Nome')
    cpf = models.CharField(max_length=14, verbose_name='CPF', validators=[validate_cpf])
    email = models.EmailField(verbose_name='E-mail', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Telefone', blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Criado em')
    paid = models.BooleanField(default=False, verbose_name='Pago')
    
    class Meta:
        verbose_name_plural='inscrições'
        verbose_name='inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return r('subscriptions:detail', self.pk)

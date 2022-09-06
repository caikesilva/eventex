from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=155, verbose_name='Nome')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Criado em')
    paid = models.BooleanField(default=False, verbose_name='Pago')
    
    class Meta:
        verbose_name_plural='inscrições'
        verbose_name='inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

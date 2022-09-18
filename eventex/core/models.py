from django.db import models
from django.shortcuts import resolve_url as r

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    slug = models.SlugField(verbose_name='Slug')
    description = models.TextField(verbose_name='Descrição', blank=True)
    photo = models.URLField(verbose_name='Foto')
    website = models.URLField(verbose_name='Website', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
    

class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Phone'),
    )
    
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE, verbose_name='Palestrante')
    kind = models.CharField(max_length=1, choices=KINDS, verbose_name='Tipo')
    value = models.CharField(max_length=255, verbose_name='Valor')

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value
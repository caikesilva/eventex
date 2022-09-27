# Generated by Django 4.0.6 on 2022-09-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_talk_options_alter_talk_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='Início')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.speaker', verbose_name='Palestrantes')),
            ],
            options={
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras',
                'abstract': False,
            },
        ),
    ]
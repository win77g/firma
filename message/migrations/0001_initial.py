# Generated by Django 2.2.10 on 2020-03-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('message', models.TextField(blank=True, default=None, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
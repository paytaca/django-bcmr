# Generated by Django 3.1.6 on 2023-02-09 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('category', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('symbol', models.CharField(max_length=100)),
                ('decimals', models.PositiveIntegerField(default=0)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('burned', 'Burned')], default='active', max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.PositiveIntegerField(default=0)),
                ('minor', models.PositiveIntegerField(default=0)),
                ('patch', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('latest_revision', models.DateTimeField(default=django.utils.timezone.now)),
                ('tokens', models.ManyToManyField(to='bcmr.Token')),
            ],
            options={
                'verbose_name_plural': 'Registries',
            },
        ),
    ]

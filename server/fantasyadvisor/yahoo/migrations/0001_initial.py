# Generated by Django 2.0.1 on 2018-01-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('game_code', models.CharField(blank=True, default='nfl', max_length=10)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]

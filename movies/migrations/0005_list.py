# Generated by Django 3.0.3 on 2020-03-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200301_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=100, null=True)),
                ('list_movie', models.ManyToManyField(blank=True, to='movies.movie')),
            ],
        ),
    ]

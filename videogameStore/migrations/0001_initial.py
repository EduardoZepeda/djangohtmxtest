# Generated by Django 3.2.4 on 2021-06-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videogame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('genre', models.CharField(choices=[('HOR', 'Horror'), ('RPG', 'RPG'), ('ADV', 'Adventure')], max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]

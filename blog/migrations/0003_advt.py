# Generated by Django 2.2.16 on 2020-10-31 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_movies_advt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advt', models.ImageField(upload_to='')),
            ],
        ),
    ]
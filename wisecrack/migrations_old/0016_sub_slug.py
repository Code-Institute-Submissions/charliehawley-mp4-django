# Generated by Django 3.2 on 2022-04-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisecrack', '0015_alter_sub_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='slug',
            field=models.SlugField(default='sub_new', max_length=200),
        ),
    ]
# Generated by Django 3.2 on 2022-04-06 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisecrack', '0011_alter_sub_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sub',
            options={'ordering': ['-created_on']},
        ),
    ]
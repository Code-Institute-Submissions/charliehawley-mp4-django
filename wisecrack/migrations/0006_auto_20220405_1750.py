# Generated by Django 3.2 on 2022-04-05 17:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wisecrack', '0005_alter_prompt_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='subs_total',
            field=models.ManyToManyField(blank=True, related_name='prompt_sub', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sub',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
# Generated by Django 3.2 on 2022-04-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wisecrack', '0017_auto_20220407_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='prompt',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wisecrack.prompt'),
        ),
    ]
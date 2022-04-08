# Generated by Django 3.2 on 2022-04-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wisecrack', '0018_alter_sub_prompt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompt',
            name='subs_total',
        ),
        migrations.AlterField(
            model_name='sub',
            name='prompt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisecrack.prompt', to_field='slug'),
        ),
    ]
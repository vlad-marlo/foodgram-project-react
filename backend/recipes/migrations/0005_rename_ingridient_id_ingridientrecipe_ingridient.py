# Generated by Django 3.2.13 on 2022-06-21 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_tag_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingridientrecipe',
            old_name='ingridient_id',
            new_name='ingridient',
        ),
    ]

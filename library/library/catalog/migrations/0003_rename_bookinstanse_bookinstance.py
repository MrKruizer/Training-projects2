# Generated by Django 4.2 on 2023-04-24 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_lang'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookInstanse',
            new_name='BookInstance',
        ),
    ]

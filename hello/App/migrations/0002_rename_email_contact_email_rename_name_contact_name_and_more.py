# Generated by Django 4.0.3 on 2022-04-30 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='company',
        ),
    ]

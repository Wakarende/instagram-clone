# Generated by Django 3.2.3 on 2021-05-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0008_follow_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]
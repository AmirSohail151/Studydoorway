# Generated by Django 3.1.2 on 2020-10-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='assig_img',
            new_name='upload_img',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='instruction',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-06 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_auto_20200306_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='submission_id',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]

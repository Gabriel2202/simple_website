# Generated by Django 4.0.8 on 2023-03-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendfiles_app', '0003_alter_receive_thefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receive',
            name='thefile',
            field=models.FileField(upload_to=''),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_user_bussiness_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
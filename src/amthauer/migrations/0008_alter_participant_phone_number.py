# Generated by Django 4.2.1 on 2023-06-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amthauer', '0007_alter_participant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
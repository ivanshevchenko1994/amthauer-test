# Generated by Django 4.2.1 on 2023-06-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amthauer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='age',
        ),
        migrations.RemoveField(
            model_name='question',
            name='section',
        ),
        migrations.RemoveField(
            model_name='session',
            name='examiner_name',
        ),
        migrations.AddField(
            model_name='answer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]

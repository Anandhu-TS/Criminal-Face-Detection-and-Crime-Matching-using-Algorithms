# Generated by Django 5.0.6 on 2024-09-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theusers', '0002_alter_case_petitionercontact_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='aadharno',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='publiccase',
            name='aadharno',
            field=models.CharField(max_length=12),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artifacts', '0002_alter_artifacts_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifacts',
            old_name='set_id',
            new_name='set',
        ),
        migrations.AlterField(
            model_name='artifacts',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='artifacts',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

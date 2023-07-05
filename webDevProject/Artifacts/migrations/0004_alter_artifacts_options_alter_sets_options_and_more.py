# Generated by Django 4.2.2 on 2023-06-09 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Artifacts', '0003_rename_set_id_artifacts_set_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artifacts',
            options={'verbose_name': 'Артефакты', 'verbose_name_plural': 'Артефакты'},
        ),
        migrations.AlterModelOptions(
            name='sets',
            options={'verbose_name': 'Комплекты', 'verbose_name_plural': 'Комплекты'},
        ),
        migrations.AddField(
            model_name='sets',
            name='bonus',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

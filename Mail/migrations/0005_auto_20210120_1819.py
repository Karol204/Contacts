# Generated by Django 3.1.5 on 2021-01-20 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0004_remove_person_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='adress',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Mail.adress'),
        ),
        migrations.AlterField(
            model_name='adress',
            name='flat_number',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]

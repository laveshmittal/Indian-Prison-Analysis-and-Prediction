# Generated by Django 2.2.5 on 2019-09-29 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_escapes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodofsentence',
            old_name='age_16_18',
            new_name='age_16_18_years',
        ),
        migrations.RenameField(
            model_name='periodofsentence',
            old_name='age_18_30',
            new_name='age_18_30_years',
        ),
        migrations.RenameField(
            model_name='periodofsentence',
            old_name='age_30_50',
            new_name='age_30_50_years',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-31 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0009_alter_write_content_alter_write_create_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write',
            name='create_content',
            field=models.TextField(),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DespensaFabi', '0003_alter_producto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]

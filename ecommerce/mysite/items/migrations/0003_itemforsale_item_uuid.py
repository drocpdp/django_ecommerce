# Generated by Django 4.2.3 on 2023-07-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_category_options_alter_itemforsale_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemforsale',
            name='item_uuid',
            field=models.TextField(default='8d7ea758-3355-4edf-a21b-4412835a7a04', max_length=30),
        ),
    ]

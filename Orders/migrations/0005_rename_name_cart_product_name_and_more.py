# Generated by Django 4.0 on 2022-04-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_remove_category_name_remove_category_selling_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='price',
            new_name='product_price',
        ),
        migrations.AddField(
            model_name='cart',
            name='user_name',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]

# Generated by Django 4.0 on 2022-05-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_remove_cart_user_name_cart_login_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='pro_image',
            field=models.ImageField(upload_to='Images/Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='Images/Products'),
        ),
    ]
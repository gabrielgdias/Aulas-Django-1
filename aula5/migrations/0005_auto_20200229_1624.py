# Generated by Django 3.0.3 on 2020-02-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula5', '0004_carrinho_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
    ]

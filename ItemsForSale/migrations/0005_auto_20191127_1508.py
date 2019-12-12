# Generated by Django 2.2.5 on 2019-11-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsForSale', '0004_auto_20191127_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='Condition',
            field=models.CharField(blank=True, choices=[('MINT', 'Mint'), ('AMAZING', 'Amazing'), ('GOOD', 'Good'), ('BAD', 'Bad'), ('TERRIBLE', 'Terrbile')], default='MINT', max_length=16, null=True, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='Condition',
            field=models.CharField(blank=True, choices=[('MINT', 'Mint'), ('AMAZING', 'Amazing'), ('GOOD', 'Good'), ('BAD', 'Bad'), ('TERRIBLE', 'Terrible')], default='MINT', max_length=16, null=True, verbose_name='Condition'),
        ),
    ]

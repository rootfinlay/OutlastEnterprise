# Generated by Django 2.2.5 on 2019-11-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemsForSale', '0003_auto_20191127_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessories',
            name='Condition',
            field=models.CharField(blank=True, choices=[('MINT', 'Mint'), ('AMAZING', 'Amazing'), ('GOOD', 'Good'), ('BAD', 'Bad'), ('TERRIBLE', 'Terrbile')], default='MINT', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='clothing',
            name='Condition',
            field=models.CharField(blank=True, choices=[('MINT', 'Mint'), ('AMAZING', 'Amazing'), ('GOOD', 'Good'), ('BAD', 'Bad'), ('TERRIBLE', 'Terrible')], default='MINT', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='shoes',
            name='Condition',
            field=models.CharField(blank=True, choices=[('MINT', 'Mint'), ('AMAZING', 'Amazing'), ('GOOD', 'Good'), ('BAD', 'Bad'), ('TERRIBLE', 'Terrible')], default='MINT', max_length=16, null=True),
        ),
    ]

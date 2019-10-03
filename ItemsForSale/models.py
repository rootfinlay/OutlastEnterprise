from django.db import models

# Create your models here.
class Clothing(models.Model):
    ITEM_CONDITION = [('MINT','Mint') , ('AMAZING','Amazing') ,  ('GOOD','Good') , ('BAD','Bad') , ('TERRIBLE','Terrible')]
    Type = models.CharField(max_length=30, verbose_name='Type of clothing:')
    Brand = models.CharField(max_length=30, verbose_name='Brand of item')
    Price = models.CharField(max_length=30, verbose_name='Price of item')
    Description = models.CharField(max_length=255, verbose_name='Description of item')

    class Meta:
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothing'

    def __str__(self):
        return self.Brand + ' ' + self.Type

class Shoes(models.Model):
    ITEM_CONDITION = [('MINT','Mint') , ('AMAZING','Amazing') ,  ('GOOD','Good') , ('BAD','Bad') , ('TERRIBLE','Terrible')]
    Type = models.CharField(max_length=30, verbose_name='Type of shoe:')
    Brand = models.CharField(max_length=30, verbose_name='Brand of shoe')
    Price = models.CharField(max_length=30, verbose_name='Price of shoe')
    Description = models.CharField(max_length=255, verbose_name='Description of shoe')

    class Meta:
        verbose_name = 'Shoe'
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return self.Brand + ' ' + self.Type

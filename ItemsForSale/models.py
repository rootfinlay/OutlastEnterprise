from django.db import models

# Create your models here.
class Clothing(models.Model):
    ITEM_CONDITION = [('MINT','Mint') , ('AMAZING','Amazing') ,  ('GOOD','Good') , ('BAD','Bad') , ('TERRIBLE','Terrible')]
    Type = models.CharField(max_length=30, verbose_name='Type of clothing:')
    Brand = models.CharField(max_length=50, verbose_name='Brand of item')
    Price = models.CharField(max_length=30, verbose_name='Price of item')
    Description = models.CharField(max_length=255, verbose_name='Description of item')
    Picture = models.ImageField(null=True, blank=True)
    Condition = models.CharField(choices=ITEM_CONDITION, max_length=16, default='MINT', null=True, blank=True, verbose_name='Condition')

    class Meta:
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothing'

    def __str__(self):
        return self.Brand + ' ' + self.Type

class Shoes(models.Model):
    ITEM_CONDITION = [('MINT','Mint') , ('AMAZING','Amazing') ,  ('GOOD','Good') , ('BAD','Bad') , ('TERRIBLE','Terrible')]
    shoe_type = models.CharField(max_length=30, verbose_name='Type of shoe:')
    shoe_brand = models.CharField(max_length=30, verbose_name='Brand of shoe')
    shoe_price = models.CharField(max_length=30, verbose_name='Price of shoe')
    shoe_description = models.CharField(max_length=255, verbose_name='Description of shoe')
    shoe_picture = models.ImageField(null=True, blank=True)
    shoe_condition = models.CharField(choices=ITEM_CONDITION, max_length=16, default='MINT', null=True, blank=True)

    class Meta:
        verbose_name = 'Shoe'
        verbose_name_plural = 'Shoes'

    def __str__(self):
        return self.shoe_brand + ' ' + self.shoe_type

class Accessories(models.Model):
    ITEM_CONDITION = [('MINT', 'Mint') , ('AMAZING', 'Amazing') , ('GOOD', 'Good') , ('BAD', 'Bad') , ('TERRIBLE', 'Terrbile')]
    accessory_type = models.CharField(max_length=30, verbose_name='Type of accessory')
    accessory_brand = models.CharField(max_length=30, verbose_name='Brand of accessory')
    accessory_price = models.CharField(max_length=30, verbose_name='Price of accessory')
    accessory_description = models.CharField(max_length=255, verbose_name='Description of accessory.')
    accessory_picture = models.ImageField(null=True, blank=True)
    accessory_condition = models.CharField(choices=ITEM_CONDITION, max_length=16, default='MINT', null=True, blank=True, verbose_name='Condition')

    class Meta:
        verbose_name = 'Accessory'
        verbose_name_plural = 'Accessories'

    def __str__(self):
        return self.Brand + ' ' + self.Type

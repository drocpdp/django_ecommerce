from django.db import models

class Category(models.Model):

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    category_name = models.TextField(max_length=50, null=False)
    category_description = models.TextField(max_length=1000, null=False)


class ItemForSale(models.Model):

    def __str__(self):
        return self. item_name
    
    class Meta:
        verbose_name = "Item for sale"
        verbose_name_plural = "Items for sale"
    
    item_name = models.TextField(max_length=100, null=False)
    item_description = models.TextField(max_length=1000, null=False)
    item_categories = models.ManyToManyField(Category)
    item_price = models.DecimalField(decimal_places=2,
                                     max_digits=10,
                                     null=False
    )



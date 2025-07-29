from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='subcategories',
                               blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f"{self.name}: {self.parent}"
        return f"{self.name}"


class Product(models.Model):
    name
    price
    unit ( kg, dona, box, liter, )
    discount
    category -

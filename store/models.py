from django.db import models


# categories = Category.objects.all()
# for category in categories:
#     print(category.name)
#     print(category.subcategories)  # related_name

class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='subcategories',
                               blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f"{self.name}: {self.parent}"
        return f"{self.name}"

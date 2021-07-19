from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'categories'
	
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

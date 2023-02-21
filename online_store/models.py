from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Title")
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name="Description")

    def __str__(self):
        return f"{self.title} - {self.description}"

class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Title")
    description = models.TextField(max_length=200, null=True, blank=False, verbose_name="Description", default="No Description")
    category = models.ForeignKey(Category, verbose_name='Category', null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date and time created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date and time updated")
    price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Price")
    image = models.CharField(max_length=500, null=False, blank=False, verbose_name="Image")

    def __str__(self):
        return f"{self.title} - {self.description}"

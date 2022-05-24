from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_category', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.title}'
        return self.title

class Difficulty(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_difficulty', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.title}'
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='product')
    description = models.TextField(blank=True)
    point = models.PositiveIntegerField(default=0)
    difficulty = models.ForeignKey(Difficulty, null=True, on_delete=models.SET_NULL, related_name='product')
    hint = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/product-detail/{self.id}/'

    def save(self, *args, **kwargs):
        self.name = self.title
        super(Product, self).save(*args, **kwargs)




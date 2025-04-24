from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    @property
    def meals(self):
        return self.meal_set.all()  # Access related meals

class Meal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='meals/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='meals', blank=True)

    def __str__(self):
        return self.name
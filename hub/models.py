from django.db import models


class ClothingBrand(models.Model):
    """An affordable clothing brand."""
    brand_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class LocalEvent(models.Model):
    """A local event."""
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    specification = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name


class Recipe(models.Model):
    """A budget recipe."""
    recipe_name = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.IntegerField()

    def __str__(self):
        return self.recipe_name


class FoodCentre(models.Model):
    """A cafe or restaurant."""
    cafe_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.cafe_name


class Other(models.Model):
    """Other products (e.g. electronics, etc.)."""
    product_name = models.CharField(max_length=200)
    shop_location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.product_name

class UpcomingMegaSale(models.Model):
    """An upcoming mega sale, linked to a clothing brand."""
    brand = models.ForeignKey('ClothingBrand', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.IntegerField(help_text="Enter discount percentage, e.g. 30")

    def __str__(self):
        return f'{self.brand} sale ({self.discount}% off)'
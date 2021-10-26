from django.db import models

class Project(models.Model):
   
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    images = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

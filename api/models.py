from django.db import models

# Create your models here.
class Pipeline(models.Model):
    top_value = models.DecimalField(max_digits=20, decimal_places=2)
    bottom_value = models.DecimalField(max_digits=20, decimal_places=4)
    symbol = models.CharField(max_length=10)
    current_value = models.DecimalField(max_digits=20 , decimal_places=4)
    created_at = models.DateField(auto_now_add=True)
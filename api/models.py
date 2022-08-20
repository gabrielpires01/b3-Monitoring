from django.db import models

# Create your models here.
class Pipeline(models.Model):
    top_value = models.DecimalField(..., decimal_places=4)
    bottom_value = models.DecimalField(..., decimal_places=4)
    symbol = models.CharField()
    current_value = models.DecimalField(..., decimal_places=4)
    created_at = models.DateField(auto_now_add=True)
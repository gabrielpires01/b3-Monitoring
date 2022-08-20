from django.db import models

# Create your models here.
class Pipeline(models.Model):
    ONE = '1min'
    FIVE =  '5min'
    FIFTEEN = '15min'
    HALF = '30min'
    HOUR = '60min'
    INTERVAL_CHOICES = [
        (ONE, '1min'),
        (FIVE, '5min'),
        (FIFTEEN, '15min'),
        (HALF, '30min'),
        (HOUR, '60min'),
    ]

    top_value = models.DecimalField(max_digits=20, decimal_places=4)
    bottom_value = models.DecimalField(max_digits=20, decimal_places=4)
    symbol = models.CharField(max_length=10)
    current_value = models.DecimalField(max_digits=20 , decimal_places=4)
    interval = models.CharField(max_length=5,choices=INTERVAL_CHOICES)
    created_at = models.DateField(auto_now_add=True)
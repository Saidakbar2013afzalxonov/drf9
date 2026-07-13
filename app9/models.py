from django.db import models

# Create your models here.
class Phones(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(blank = False, null = False)
    description = models.TextField()
    created_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
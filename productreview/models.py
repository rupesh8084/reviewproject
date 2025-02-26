from django.db import models
import uuid
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)  # Name of the item
    description = models.TextField(blank=True, null=True)  # Optional description
    link = models.URLField(max_length=500, blank=True, null=True)  # URL link
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Image upload

    def __str__(self):
        return self.name  # Display name in Django Admin
    

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} - {self.rating} stars"
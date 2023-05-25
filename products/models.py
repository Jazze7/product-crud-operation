from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to="images/products/")
    status=models.BooleanField(default=True)

    user=models.ForeignKey("auth.User",on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name
from django.db import models
import uuid


class Katigoriya(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Mahsulot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    discription = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_length=50, max_digits=10, decimal_places=2)
    stock_products = models.IntegerField()
    catigory = models.ForeignKey(Katigoriya, related_name='mahsulotlar', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

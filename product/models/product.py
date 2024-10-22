from api.models import AutoTimeStamp, AuditUser
from django.db import models
from product.constants.product import ProductRating
class Product(AutoTimeStamp, AuditUser):
    name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    description = models.TextField(default="")
    rating = models.FloatField(default=ProductRating.NONE)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0) # tong so luong danh gia
    total_sold = models.IntegerField(default=0) # tong so da ban

    class Meta:
        db_table = "s_product"
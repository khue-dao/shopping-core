from api.models import AutoTimeStamp, AuditUser
from .product import Product
from .category import Category
from django.db import models
class CategoryTagging(AutoTimeStamp, AuditUser):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "s_category_tagging"
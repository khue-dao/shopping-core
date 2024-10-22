from api.models import AutoTimeStamp, AuditUser
from django.db import models
from .product import Product
from product.constants.product import ProductAttributeType as ProductAttibuteTypeConst
from .product_attibute_name import ProductAttributeName
class ProductAttribute(AutoTimeStamp, AuditUser):
    attribute_name = models.ForeignKey(ProductAttributeName, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.SmallIntegerField(default=ProductAttibuteTypeConst.DEFAULT)
    value = models.TextField(max_length=255, default="")
    attibute_name = models.TextField(max_length=255, default="")

    class Meta:
        db_table = "s_product_attribute"
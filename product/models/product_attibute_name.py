from api.models import AutoTimeStamp, AuditUser
from django.db import models

class ProductAttributeName(AutoTimeStamp, AuditUser):
    name = models.CharField(max_length=255) # name = Mau sac

    class Meta:
        db_table = "s_product_attribute_type"
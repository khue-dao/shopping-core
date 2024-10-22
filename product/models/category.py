from api.models import AutoTimeStamp, AuditUser
from django.db import models

class Category(AutoTimeStamp, AuditUser):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField(default=0)

    class Meta:
        db_table = "s_category"
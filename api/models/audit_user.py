from .base import BaseModel
from django.db import models

class AuditUser(BaseModel):
    created_by = models.IntegerField(default=0)
    updated_by = models.IntegerField(default=0)
    
    class Meta:
        abstract = True
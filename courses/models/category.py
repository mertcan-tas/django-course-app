from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True)

    def __str__(self):
        return self.name
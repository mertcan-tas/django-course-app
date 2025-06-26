from django.db import models
from autoslug import AutoSlugField

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)
    is_active = models.BooleanField(default=True, null=False)
    category = models.ForeignKey("courses.Category", on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course_details", kwargs={"slug": self.slug})

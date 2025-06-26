from django.contrib import admin

from courses.models import Course, Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active",)
    list_display_links = ("title",)
    readonly_fields = ("slug",)
    list_filter = ("title", "is_active",)
    list_editable = ("is_active",)
    search_fields = ("is_active",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    search_fields = ("name",)
    readonly_fields = ("slug",)

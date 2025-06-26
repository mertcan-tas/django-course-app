from django import template
from courses.models import Category

register = template.Library()

@register.inclusion_tag('courses/partials/_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def add_class(widget_html, class_name):
    if 'type="checkbox"' in widget_html:
        return widget_html
    
    if 'class="' in widget_html:
        return widget_html.replace('class="', f'class="{class_name} ')
    else:
        return widget_html.replace('<input', f'<input class="{class_name}"')


@register.filter
def add_invalid_class(widget_html):
    return mark_safe(add_class(widget_html, "form-control is-invalid"))

@register.filter
def add_form_control(widget_html):
    return mark_safe(add_class(widget_html, "form-control"))

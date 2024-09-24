from django import template

# Register the template library
register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """Adds a CSS class to form fields in Django templates."""
    return field.as_widget(attrs={"class": css})

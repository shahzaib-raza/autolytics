from django import template

register = template.Library()


@register.simple_tag
def tag1():
    return "This is a custom tag"

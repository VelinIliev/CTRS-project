from django.template import Library
from datetime import datetime, timedelta

register = Library()


@register.filter
def placeholder(field, value):
    field.field.widget.attrs['placeholder'] = value
    return field


@register.filter
def autofocus(field):
    field.field.widget.attrs['autofocus'] = True
    return field



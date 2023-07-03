from django import template

register = template.Library()


@register.filter(name='convert_to_list')
def image_data(object):
    new_list = []
    for x in object.split(", "):
        x = x.replace("'", "").replace("[", "").replace("]", "")
        new_list.append(x)
    return new_list

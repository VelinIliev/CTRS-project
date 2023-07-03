from django import template

register = template.Library()


@register.filter(name='convert_to_list')
def image_data(object):
    new_list = []
    for x in object.split(", "):
        x = x.replace("'", "").replace("[", "").replace("]", "")
        new_list.append(x)
    print(new_list)
    return new_list

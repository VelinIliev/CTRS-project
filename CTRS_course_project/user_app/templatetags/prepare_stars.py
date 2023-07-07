from django.template import Library

register = Library()


@register.filter
def prepare_stars(rating):
    stars = []
    full_stars = int(rating // 1)
    half_star = int((rating - full_stars) * 10)
    empty_stars = 10 - full_stars - 1

    for star in range(full_stars):
        stars.append(f'images/stars/star10.svg')

    if half_star > 0:
        stars.append(f'images/stars/star{half_star}.svg')
    else:
        stars.append(f'images/stars/star00.svg')

    for star in range(empty_stars):
        stars.append(f'images/stars/star00.svg')

    return stars

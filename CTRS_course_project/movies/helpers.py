from CTRS_course_project.movies.models import MovieVotes


def calculate_runtime(value):
    hours = value // 60
    minutes = value - hours * 60
    if hours > 0:
        return f'{hours}h {minutes}min'
    return f'{minutes}min'


def calculate_rating(movie):
    sum_rating = MovieVotes.objects.filter(movie=movie)
    sum_rating = sum([x.rating for x in sum_rating])
    votes_count = MovieVotes.objects.filter(movie=movie).count()
    if sum_rating == 0:
        rating = 0
    else:
        rating = sum_rating / votes_count
    return rating


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


def displays_stars(user_rating):
    stars = []
    if user_rating:
        for star in range(user_rating.rating):
            stars.append(f'images/stars/star10.svg')
        for star in range(10 - user_rating.rating):
            stars.append(f'images/stars/star00.svg')
    else:
        for star in range(10):
            stars.append(f'images/stars/star00.svg')
    return stars


def find_vote(movie, user):
    try:
        already_voted = MovieVotes.objects.filter(movie=movie, user=user).get()
    except MovieVotes.DoesNotExist:
        already_voted = None
    return already_voted

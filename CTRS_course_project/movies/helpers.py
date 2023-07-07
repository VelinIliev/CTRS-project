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


def find_vote(movie, user):
    try:
        already_voted = MovieVotes.objects.filter(movie=movie, user=user).get()
    except MovieVotes.DoesNotExist:
        already_voted = None
    return already_voted

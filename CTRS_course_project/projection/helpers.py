import datetime

from CTRS_course_project.movies.models import Movie
from CTRS_course_project.projection.models import Seat, Projection


def create_seats(hall):
    seats = []
    for row in range(1, hall.rows + 1):
        new_row = []
        for seat in range(1, hall.seats_per_row + 1):
            new_row.append(f'{row:02d}-{seat:02d}')
        seats.append(new_row)
    return seats


def get_seats(instance):
    seats = Seat.objects.filter(projection_id=instance.id).order_by('row_n', 'seat_n')
    final_seats = []
    new_row = []
    for row in range(0, instance.hall.rows * instance.hall.seats_per_row):
        if (row + 1) % instance.hall.rows != 0:
            new_row.append(seats[row])
        else:
            new_row.append(seats[row])
            final_seats.append(new_row)
            new_row = []
    return final_seats


def find_free_seats(projection_pk):
    free_seats = Seat.objects.filter(projection_id=projection_pk, is_taken=0).count()
    if free_seats > 0:
        return f'{free_seats} free seats'
    else:
        return 'No free seats'


def get_today_movies(day):
    this_day = Projection.objects.filter(date=day).order_by('hour')

    list_of_movies = {}
    for projection in this_day:
        movie = Movie.objects.filter(pk=projection.movie_id).get()
        if movie.title not in list_of_movies:
            list_of_movies[movie.title] = {
                'movie': movie,
                'hours': {
                    projection.hour: {
                        'projection': projection,
                        'free_seats': find_free_seats(projection.pk),
                    }
                }
            }
        else:
            list_of_movies[movie.title]['hours'][projection.hour] = {
                'projection': projection,
                'free_seats': find_free_seats(projection.pk),
            }

    return list_of_movies or None


def get_days():
    first_day = datetime.datetime.today().date()
    days = [
        first_day,
        first_day + datetime.timedelta(days=1),
        first_day + datetime.timedelta(days=2),
        first_day + datetime.timedelta(days=3),
        first_day + datetime.timedelta(days=4),
        first_day + datetime.timedelta(days=5),
        first_day + datetime.timedelta(days=6),
    ]
    return days

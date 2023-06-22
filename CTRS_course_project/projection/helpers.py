from CTRS_course_project.projection.models import Seat


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

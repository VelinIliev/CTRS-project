def create_seats(hall):
    seats = []
    for row in range(1, hall.rows + 1):
        new_row = []
        for seat in range(1, hall.seats_per_row + 1):
            new_row.append(f'{row:02d}-{seat:02d}')
        seats.append(new_row)
    return seats
    # print([[f'{r:02d}-{s:02d}' for s in range(1, 11)] for r in range(1, 11)])

# create_seats()
def calculate_runtime(value):
    hours = value // 60
    minutes = value - hours * 60
    if hours > 0:
        return f'{hours}h {minutes}min'
    return f'{minutes}min'

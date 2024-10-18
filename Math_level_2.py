def calculate_point(speed, time):
    max_distance = 109
    position = (speed * time) % max_distance
    return position

print(calculate_point(80,10))
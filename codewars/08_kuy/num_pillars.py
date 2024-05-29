def distance_between_pillars(number_of_pillars, distance_between_pillars, width_of_pillar):
    if number_of_pillars < 1 or distance_between_pillars < 10 or distance_between_pillars > 30 or width_of_pillar < 10 or width_of_pillar > 50:
        return 0

    return (number_of_pillars - 1) * distance_between_pillars - (number_of_pillars - 2) * width_of_pillar

print(distance_between_pillars(5, 20, 15))  # Output: 80
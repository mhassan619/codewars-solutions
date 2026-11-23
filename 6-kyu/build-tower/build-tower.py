def tower_builder(n_floors):
    tower = []
    for i in range(1,n_floors+1):
        spaces = n_floors - i
        stars = 2 * i - 1
        floor = (" " * spaces) + ("*" * stars) + (" " * spaces)
        tower.append(floor)
    return tower
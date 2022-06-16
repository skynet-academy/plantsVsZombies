def collision_with_zombies(plants, zombies, spawns_suns, peas, Sun, lawns):
    for plant in plants:
        if(plant.add_sun):
            sun = Sun(plant.center_x + 20, plant.center_y + 30)
            self.spawns_suns.append(sun)
            plant.add_sun = False

        if(plant.add_pea):
            pea = Pea(plant.center_x + 10, plant.center_y + 10)
            peas.append(pea)
            plant.add_pea = False

        if(plant.is_dead):
            lawns.remove((plant.line, plant.column))

        zombies = check_for_collision_with_list(plant, self.zombies)

        for zombie in zombies:
            zombie.eating = True

def collision_with_plants(plants, zombies):
    pass

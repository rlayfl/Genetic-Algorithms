# Richard Lay-Flurrie
# 21/02/24

# This is my attempt at a genetic algorithm to best store model tanks on a shelf making the most efficient use
# of the space.

# I am assuming they are all 1:72 scale for this. 

import random

from model_tank import ModelTank

models = [
    ModelTank("Firefly", 10, 4),
    ModelTank("Churchill", 8, 5),
    ModelTank("Stuart", 5, 3)
]

# Set values for the space we have available

shelf_width = 10
shelf_length = 30
shelf_surface_area_in_square_inch = shelf_width * shelf_length

population_side = 30
mutation_rate = 0.1
generations = 100

# Create population 
def generate_population(population_size):
    return [[random.randint(0, 3) for _ in range(len(models))] for _ in range(population_size)]

# Fitness function 
def fitness(models):

    # Our fitness is defined by the amount of space taken up in total / amount of tanks on display
    space_taken_up_in_square_inch = 0

    for model in models:

        x_of_front_left = 0
        y_of_front_left = 0

        x_of_rear_right = 0
        y_of_rear_right = 0

        print("Tank::")
        print(model.name)
        print(str(model.length) + " units long")
        print(str(model.width) + " units long")

        space_taken_up_in_square_inch += (model.length * model.width)

    return space_taken_up_in_square_inch

def main():
    print(":: Starting")
    fitness(models)

if __name__ == "__main__":
    main()
from models.hamster import Hamster

# input data
hamsters = []
def input_data(filename):
    with open(filename, "r") as file:
        food_storage = int(file.readline())
        available_hamsters = int(file.readline())

        for line in file.readlines():
            norm, greed = line.split()
            hamsters.append(Hamster(int(norm), int(greed)))

    return { "food_storage": food_storage, "available_hamsters": available_hamsters, "hamsters": hamsters }


# output data
def output_data(filename, value):
    with open(filename, "w") as file:
        file.write(str(value))
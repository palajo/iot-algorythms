from csv import input_data, output_data


# input file
filename = "hamster3.csv"
data = input_data("data/input/" + filename)


# given
food_storage = data["food_storage"]
available_hamsters = data["available_hamsters"]
hamsters = data["hamsters"]


# sort hamsters and append in 2d array
hamsters_appetite = []
index = -1

for hamster in hamsters:
    hamsters_appetite.append([])
    index += 1

    for hamster in hamsters:
        hamsters_appetite[index].append(hamster.greed * (index) + hamster.norm)
    
    hamsters_appetite[index].sort()


# purchasing hamster while enough food
checked_hamsters = 0
puchased_hamsters = 0

while (food_storage > 0) and (checked_hamsters < available_hamsters):
    checked_hamsters += 1 

    if sum(hamsters_appetite[checked_hamsters - 1][:checked_hamsters]) <= food_storage:
        puchased_hamsters += 1


# results
print("We could afford %d hamster(s)" % puchased_hamsters)
output_data("data/output/" + filename, puchased_hamsters)
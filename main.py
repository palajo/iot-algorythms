import time
from decimal import Decimal

from write.write_to_csv import write_to_csv

from models.domcrat import Domcart
from sort.bubble_sort import bubble_sort
from sort.merge_sort import merge_sort


# creating domcracts array
domcrats = []
domcrats.append(Domcart(2000, "BMW", "Black", 25))
domcrats.append(Domcart(3000, "Mercedes-Benz", "White", 50))
domcrats.append(Domcart(2200, "Audi", "Brown", 40))
domcrats.append(Domcart(3500, "Ferrari", "Red", 15))
domcrats.append(Domcart(4000, "Rolls-Royce", "Black", 50))



# creating domcrats max_weight array
domcrats_max_weight = []

for domcrat in domcrats:
    domcrats_max_weight.append(domcrat.max_weight)


# creating domcrats weight array
domcrats_weight = []

for domcrat in domcrats:
    domcrats_weight.append(domcrat.weight)


# bubble_sort for max_weight
bubble_execution_start = time.time()
bubble_sort(domcrats_max_weight)
bubble_execution_end = time.time()
bubble_execution_time = bubble_execution_end - bubble_execution_start

print("\nBubble sorted array of max_weight (execution time: %f)" % bubble_execution_time)
print("Comparisons: {}\nSwaps: {}".format(bubble_sort.comparisones, bubble_sort.swaps))
for i in range(len(domcrats_max_weight)):
    print(domcrats_max_weight[i])


# mergre_sort for weight
merge_execution_start = time.time()
merge_sort(domcrats_weight)
merge_execution_end = time.time()
merge_execution_time = merge_execution_end - merge_execution_start

print("\nMerge sorted array of weight (execution time: %f)" % merge_execution_time)
print("Comparisons: {}\nSwaps: {}".format(merge_sort.comparisones, merge_sort.swaps))
for i in range(len(domcrats_weight)):
    print(domcrats_weight[i])


# write data to CSV file
write_array = []

write_array.append("Bubble sort")
write_array.append(bubble_sort.comparisones)
write_array.append(bubble_sort.swaps)
write_array.append(Decimal(bubble_execution_time))

for i in domcrats_max_weight:
    write_array.append(i)

write_array.append("Merge sort")
write_array.append(merge_sort.comparisones)
write_array.append(merge_sort.swaps)
write_array.append(Decimal(merge_execution_time))

for i in domcrats_weight:
    write_array.append(i)

write_to_csv(write_array)

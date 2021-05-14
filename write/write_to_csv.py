
import csv

def write_to_csv(arr):
    with open('./write/output/output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(map(lambda x: [x], arr))

            


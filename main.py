from methods.output_data import output_data
from methods.input_data import input_data


# input data
vertexes, connections, clients, requests = input_data('csv/input/gamsrv1.csv')

# output data
result = "No result for now, only problems!"
output_data('csv/output/gamsrv1.csv', result)
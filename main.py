from models.Graph import Graph
from methods.dijkstra import dijkstra
from methods.output_data import output_data
from methods.input_data import input_data


# input data
nodes, connections, clients, graph = input_data('csv/input/gamsrv1.csv')


# dijkstra
Graph.print_graph(graph)


# output data
result = "No result for now, only problems!"
output_data('csv/output/gamsrv1.csv', result)
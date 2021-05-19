from models.Graph import Graph


def input_data(filename):

    graph = Graph()

    with open(filename, 'r') as file:
        lines = file.readlines()

        nodes, connections = (int(x) for x in lines[0].split())
        clients = (int(x) for x in lines[1].split())

        for line in lines[2:]:
            start_vertex, end_vertex, ping = (int(x) for x in line.split())
            graph.create_edges(start_vertex, end_vertex, ping)

    return nodes, connections, clients, graph
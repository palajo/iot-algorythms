def input_data(filename):

    with open(filename, 'r') as file:
        lines = file.readlines()

        vertexes, connections = tuple(int(x) for x in lines[0].split())
        clients = tuple(int(x) for x in lines[1].split())

        requests = []

        for line in lines[2:]:
            requests.append(tuple(int(x) for x in line.split()))

    return vertexes, connections, clients, requests
class Graph:
    def __init__(self):
        self.connections = {}


    def create_edges(self, first_vertex, second_vertex, ping):
        self.__create_edge(first_vertex, second_vertex, ping)
        self.__create_edge(second_vertex, first_vertex, ping)


    def __create_edge(self, first_vertex, second_vertex, ping):
        if first_vertex in self.connections.keys():
            if (second_vertex, ping) not in self.connections[first_vertex]:
                self.connections[first_vertex].append((second_vertex, ping))
                
        else: 
            self.connections[first_vertex] = [(second_vertex, ping)]


    def print_graph(self):
        for x in self.connections:
            print(x, self.connections[x])
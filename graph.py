# Python 3.7


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def add_vertex(self, vertex, weight):
        if vertex not in self.__graph_dict:
            self.__graph_dict[(vertex, weight)] = []

    def add_edge(self, edge, weight):
        """ edge is a list [(index1,weight1),(index2,weight2)"""
        vertex1, vertex2 = edge[0], edge[1]
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append((vertex2, weight))
        else:
            self.__graph_dict[vertex1] = (vertex2, weight)

    def get_vertices_raw(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def get_vertices(self):
        """ returns the vertices of a graph """
        v = list(self.__graph_dict.keys())
        return [i[0] for i in v]

    def keys_values(self):
        return self.__graph_dict.keys(), self.__graph_dict.values()

    def get_edges(self, v):
        keys, values = self.keys_values()
        values = list(values)
        adj = []
        for e in values[v]:
            adj.append(e[0][0])
        return adj

    def distance(self, vi, vf):
        _, values = self.keys_values()
        values = list(values)
        dis = None
        for e in values[vi]:
            if e[0][0] == vf:
                dis = e[1] + e[0][1]
                break
        return dis

    def get_source_weight(self):
        keys = self.get_vertices_raw()
        keys = list(keys)
        w = keys[0][1]
        return w

    def __str__(self):
        keys, values = self.keys_values()
        values = list(values)
        s = ""
        for i, v in enumerate(values):
            s += "value " + str(i) + " = " + str(v) + "\n"
        return s


def dijkstra(graph, initial=0):
    visited = {initial: 0}
    vertices = set(graph.get_vertices())

    while vertices:
        min_vertex = None
        for vertex in vertices:
            if vertex in visited:
                if min_vertex is None:
                    min_vertex = vertex
                elif visited[vertex] < visited[min_vertex]:
                    min_vertex = vertex

        if min_vertex is None:
            break
        vertices.remove(min_vertex)
        current_weight = visited[min_vertex]

        for edge in graph.get_edges(min_vertex):
            weight = current_weight + graph.distance(min_vertex, edge)
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight

    return visited

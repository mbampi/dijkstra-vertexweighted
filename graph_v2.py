from collections import OrderedDict

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}     
        self.__graph_dict = graph_dict

    

    def add_vertex(self, vertex,weight):
        if vertex not in self.__graph_dict:
            self.__graph_dict[(vertex,weight)] = []
        
    def add_edge(self, edge,weight):
        "edge is a list [(index1,weight1),(index2,weight2)"
        vertex1 , vertex2 = edge[0],edge[1]
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append((vertex2,weight))
        else:
            self.__graph_dict[vertex1] = (vertex2,weight)

    def get_vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def keys_values(self):
        return self.__graph_dict.keys(),self.__graph_dict.values()

    def __str__(self):
        keys, values = self.keys_values()
        values = list(values)
        s = ""
        for i, v in enumerate(values):
            s += "value " + str(i) + " = " + str(v) + "\n"
        return s


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
            self.__graph_dict[vertex1] = [(vertex2,weight)]
    
    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges




    def get_vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def get_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()



    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


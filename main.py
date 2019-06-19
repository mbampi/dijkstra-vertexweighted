from graph import *


print("problema dos caminhos mínimos de fonte única com pesos nos vértices e nas arestas")
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_edge('A', 'B', 12)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'E', 13)
g.add_edge('E', 'B', 6)

print(dijkstra(g, 'A'))

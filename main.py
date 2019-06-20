from graph import *


print("problema dos caminhos mínimos de fonte única com pesos nos vértices e nas arestas")

n = int(input())
print(n)
vertices_destino = input().split(" ")
vertices_destino = list(map(int, vertices_destino))
print(vertices_destino)
pesos_vertices = input().split(" ")
pesos_vertices = list(map(int, pesos_vertices))
print(pesos_vertices)

matriz = []
for i in range(n):
    matriz.append(input().split(" "))
    matriz[i] = list(map(int, matriz[i]))
    print(matriz[i])

vertices = []
for i in range(n):
    vertices.append(pesos_vertices[i])

'''
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
'''

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)  # Si el grafo es no dirigido

    def imprimir_grafo(self):
        for vertice, adyacentes in self.vertices.items():
            print(f"{vertice}: {adyacentes}")

# Crear un grafo
grafo = Grafo()

# Agregar vértices
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')

# Agregar aristas
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'D')
grafo.agregar_arista('D', 'E')

# Imprimir el grafo
print("Representación del Grafo:")
grafo.imprimir_grafo()

# this is bidirectional and weighted graph
"""
in graphs we have to perform curd on graph attrubute to instance
"""
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
        self.source = None

    def __str__(self):
        return str(self.bfs(self.source))

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.source = vertex
            self.vertices[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.vertices[vertex1][vertex2] = weight
        self.vertices[vertex2][vertex1] = weight
        

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices:
            self.vertices[vertex1].pop(vertex2, None)
        if vertex2 in self.vertices:
            self.vertices[vertex2].pop(vertex1, None)


    def traverse_graph(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        for neighbor in self.vertices[start_vertex]:
            if neighbor not in visited:
                self.traverse_graph(neighbor, visited)
        return visited


    def bfs(self, source):
        visited = []
        queue = set()
        queue.add(source)
        while queue:
            m = queue.pop()
            for neighbor in self.vertices[m]:
                if neighbor not in visited:
                    queue.add(neighbor)
            visited.append(m)
        return visited


    def dfs(self, source, visited=[]):
        for neighbor in self.vertices[source]:
            if neighbor not in visited:
                visited.append(neighbor)
                self.dfs(neighbor, visited)
        return visited


    def dijkstra(self, source):
        distances = {vertex:float('inf') for vertex in self.vertices}
        distances[source] = 0
        
        Q = [(0, source)]

        while Q:
            current_dist, current_vertex = heapq.heappop(Q)

            if current_dist > distances[current_vertex]:
                    continue

            for neighbor, weight in self.vertices[current_vertex].items():
                dist = current_dist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(Q, (dist, neighbor))

        return distances

                
                

                






g = Graph()

g.add_edge(0, 1, 5) 
g.add_edge(0, 2, 3) 
g.add_edge(1, 2, 2) 
g.add_edge(1, 3, 1) 
g.add_edge(2, 3, 3)

print(g)


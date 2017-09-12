import LinkedList
from collections import deque

class Graph:
      def __init__(self, num_of_vertices, num_of_edges, directed=False):
          self.num_of_vertices
          self.num_of_edges
          self.graph = []
          for i in num_of_vertices:
              self.graph.append(LinkedList())

      def insert(self, from, to):
          self.graph[from].insert(to)

          if self.directed:
             self.graph[to].insert(from)
             
      def search(self, action):
          processed = {}
          discovered = {}
          Q = deque()
          # for each vertex
          for vertex in self.graph:
            # visit each connection
            for (cur = vertex; cur != None; cur = cur.next):
                  Q.append(vertex)
                if discovered.get(vertex) is None:
                      discoverd[vertex] = True
                      Q.append(vertex)
                      action(vertex)

                      
      def 

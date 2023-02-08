import math
from nodo import nodo

class Graph:
    def __init__(self):
        self.graph = []
        
    def addEdge(self, node, edge):
        if len(self.graph) > 0:
            # En caso de que no dxista el nodo se crea ese nodo 
            nObj = [obj for obj in self.graph if obj.value == node]
            # En caso de que no dxista el nodo se crea ese nodo 
            if not any(node == obj.value for obj in self.graph): 
                nodee = nodo(node, [edge], [], None)
                self.graph.append(nodee) 
            # Si existe la arista que se quiere agregar en 
            # la lista de dependencias de ese nodo tira error
            elif edge in nObj[0].dependencies:
                raise ValueError("Arista repetida.")
            # Sino hace append 
            else:
                nObj[0].dependencies.append(edge)          
        else:
            nodee = nodo(node, [edge], [], None)
            self.graph.append(nodee)


graph = Graph()
graph.addEdge(2, 1)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
graph.addEdge(1, 3)

for j in graph.graph:
    print(j.value, j.dependencies)


#     def notInRange(self, listt):
#         for i in listt:
#             if i < 0 or i > 1:
#                 return True
#         return False

#     def addProb(self, node, prob):
#         dep = 0 # dependencias
#         for key in self.graph:
#             if node in self.graph[key]:
#                 dep += 1
#         if len(prob) != math.pow(2, dep):
#             raise ValueError("No contiene todas las probabilidades necesarias")
#         elif self.notInRange(prob):
#             raise ValueError("Las números deben encontrarse en el rango de 0 y 1")
#         else:
#             self.probs[node] = prob
    
#     def checkConections(self):
#         for node in self.graph:
#             if len(self.graph[node]) > 0:
#                 return True
#         return False

#     def getKey(self, dict, value):
#         for key in dict:
#             if value in dict[key]:
#                 return key

#     def compactness(self):
#         for node in self.probs:
#             print(node)
#             if node in self.graph[node]: 
#                 print(node, self.getKey(self.graph, node))


#     def printGraph(self):
#         for node in self.graph:
#             print("Adjacency list {}: {}".format(node, self.graph[node]))
#         print(self.probs)



# graph = Graph()
# graph.addEdge("B", "A")
# graph.addEdge("A", "C")
# graph.addEdge("C", "A")
# graph.addEdge("A", "D")
# graph.addEdge("D", "E")
# # graph.addProb("A", [0, 0.5, 1, 0.99999])

# print(graph.graph)
# # graph.compactness()
# # graph.printGraph() 
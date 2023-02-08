import math
from nodo import nodo

class Graph:
    def __init__(self):
        self.graph = []
        
    def addEdge(self, node, edge):
        if len(self.graph) > 0:
            # En caso de que no dxista el nodo se crea ese nodo 
            nObj = [obj for obj in self.graph if obj.value == node]
            # En caso de que no exista el nodo se crea ese nodo 
            if not any(node == obj.value for obj in self.graph): 
                nodee = nodo(node, [edge], [], None)
                self.graph.append(nodee) 
                for nodeG in self.graph:
                    if nodee.value in nodeG.dependencies:
                        nodee.parent.append(nodeG.value)
            # Si existe la arista que se quiere agregar en 
            # la lista de dependencias de ese nodo tira error
            elif edge in nObj[0].dependencies:
                raise ValueError("No se puede añadir una arista repetida.")
            # Sino hace append 
            else:
                nObj[0].dependencies.append(edge)          
        else:
            nodee = nodo(node, [edge], [], None)
            self.graph.append(nodee)

    def notInRange(self, listt):
        for i in listt:
            if i < 0 or i > 1:
                return True
        return False

    def addProb(self, node, prob):
        nObj = [obj for obj in self.graph if obj.value == node]
        dep = nObj[0].dependencies  

        if len(prob) != math.pow(2, dep):
             raise ValueError("No contiene todas las probabilidades necesarias")
        elif self.notInRange(prob):
             raise ValueError("Las números deben encontrarse en un rango de 0 y 1")
        else:
            nObj[0].probabilities.append(prob)


graph = Graph()
graph.addEdge(2, 1)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
# graph.addEdge(1, 3)

for j in graph.graph:
    print(j.value, j.dependencies, j.parent)

 
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
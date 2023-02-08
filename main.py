import math
from nodo import nodo

class Graph:
    def __init__(self):
        self.graph = []
        
    def addEdge(self, node, edge):
        if len(self.graph) > 0:
            # En caso de que no dxista el nodo se crea ese nodo 
            nObj = [obj for obj in self.graph if obj.value == node]
            # En caso de que no se envie un nodo como parametro
            if not node:
                raise ValueError("Debes colocar un nodo")
            # En caso de que no exista el nodo se crea ese nodo 
            elif not any(node == obj.value for obj in self.graph):
                if not edge: 
                    nodee = nodo(node, [], [], None)
                    self.graph.append(nodee) 
                else:
                    nodee = nodo(node, [edge], [], None)
                    self.graph.append(nodee) 
                # Añadiendo nodos padre
                for nodeG in self.graph:
                    if nodee.value in nodeG.dependencies:
                        nodee.parent.append(nodeG.value)
            # Si existe la arista que se quiere agregar en 
            # la lista de dependencias de ese nodo tira error
            elif edge in nObj[0].dependencies:
                raise ValueError("No se puede añadir una arista repetida.")
            # Sino hace append 
            else:
                if edge != None:
                    nObj[0].dependencies.append(edge)          
        else:
            if not edge:
                nodee = nodo(node, [], [], None)
                self.graph.append(nodee) 
            elif not node:
                raise ValueError("Debes colocar un nodo")
            else:
                nodee = nodo(node, [edge], [], None)
                self.graph.append(nodee)

    def addProb(self, node, prob):
        nObj = [obj for obj in self.graph if obj.value == node]
        parent_s = len(nObj[0].parent)

        if len(prob) != math.pow(2, parent_s):
             raise ValueError("Cantidad incorrecta de probabilidades")
        elif not all(0 <= i <= 1 for i in prob):
             raise ValueError("Las números deben encontrarse en un rango de 0 y 1")
        else:
            nObj[0].probabilities = prob

    def checkConections(self):
        for node in self.graph:
            if not (len(node.parent) > 0 or len(node.dependencies) > 0):
                return False
        return True


    def compactness(self):
        for node in self.graph:
            if node.parent and not node.dependencies:
                for node in node.parent:
                    print()
            elif node.parent and not node.dependencies:
                pass
            elif node.parent and node.dependencies:
                pass

        

graph = Graph()
graph.addEdge("A", "C")
graph.addEdge("B", "C")
graph.addEdge("C", "D")
graph.addEdge("C", "E")
graph.addEdge("D", None)
graph.addEdge("E", None)
print(graph.checkConections())
# graph.addProb("E", [0.2, 0.5])

# for j in graph.graph:
#     print("val: ", j.value, "probs: ", j.probabilities)

for j in graph.graph:
    print("val: ", j.value, "dep: ", j.dependencies, "parent: ", j.parent)


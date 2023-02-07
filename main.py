import math

class Graph:
    def __init__(self):
        self.graph = dict()
        self.probs = dict()
        
    def addEdge(self, node, edge):
        if node in self.graph:
            self.graph[node].append(edge)
            self.probs[edge] = []
        else:
            self.graph[node] = [edge]
            self.probs[edge] = []

    def notInRange(self, listt):
        for i in listt:
            if i < 0 or i > 1:
                return True
        return False

    def addProb(self, node, prob):
        dep = 0 # dependencias
        for key in self.graph:
            if node in self.graph[key]:
                dep += 1
        if len(prob) != math.pow(2, dep):
            raise ValueError("No contiene todas las probabilidades necesarias")
        elif self.notInRange(prob):
            raise ValueError("Las números deben encontrarse en el rango de 0 y 1")
        else:
            self.probs[node] = prob
    
    def checkConections(self):
        for node in self.graph:
            if len(self.graph[node]) > 0:
                return True
        return False

    def printGraph(self):
        for node in self.graph:
            print("Adjacency list of vertex {}: {}".format(node, self.graph[node]))
        print(self.probs)



graph = Graph()
graph.addEdge("B", "A")
graph.addEdge("A", "C")
graph.addEdge("C", "A")
graph.addEdge("A", "D")
graph.addEdge("D", "A")
# graph.addProb("A", [0, 0.5, 1, 0.99999])

print(graph.ch())
graph.checkConections()
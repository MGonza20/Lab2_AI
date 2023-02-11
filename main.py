import math
from nodo import nodo
import itertools

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

    
    def genKeys(self, node):
        sim_s = []
        nodee = [obj for obj in self.graph if obj.value == node][0]
        
        if nodee.parent:
            sim_s += nodee.parent
        sim_s.append(nodee.value)
        
        # Generando posibles combinaciones de simbolos + y menos 
        # dependiendo de la cantidad de nodos
        simC = itertools.product(*[['+', '-'] for sim in sim_s])
        combis = [''.join(el) for el in simC]

        # Generando las llaves de las posibles combinaciones de simbolos
        # y añadiendolas al diccionario
        keys = []
        for i in range(len(combis)):
            key = ""
            for j in range(len(combis[i])):
                key += combis[i][j] + sim_s[j] 
            if len(key) <= 2:
                key = 'P({})'.format(key)
            else:
                key = 'P({}|{})'.format(key[-2:], key[:-2])
            keys.append(key)        
        return keys

    def checkKeys(self, dictt, listt):
        for k in dictt:
            if k not in listt:
                return False
        return True

    def checkKeysNeg(self, dictt):
        for k in dictt:
            if k[2:3] == '-':
                return [True, k[3:4]]
            return [False]


    def addProb(self, node, prob, probD):
        nObj = [obj for obj in self.graph if obj.value == node]
        parent_s = len(nObj[0].parent)
        kNeg = self.checkKeysNeg(probD)
        
        if len(probD) != math.pow(2, parent_s):
             raise ValueError("Cantidad incorrecta de probabilidades")
        elif not self.checkKeys(probD, self.genKeys(node)):
            raise ValueError("Nombre de llaves/probabilidades no permitidas")
        elif kNeg[0]:
            raise ValueError("No puedes ingresar " + kNeg[1] + " negativo")        
        elif not all(0 <= i <= 1 for i in probD.values()):
             raise ValueError("Las números deben encontrarse en un rango de 0 y 1")
        else:
            nObj[0].probabilities = prob

    def checkConections(self):
        for node in self.graph:
            if not (len(node.parent) > 0 or len(node.dependencies) > 0):
                return False
        return True


    def compactness(self):
        jointList = []
        for node in self.graph:
            if not len(node.parent):
                jointList.append(f"P({node.value})")
            else:
                concat = ",".join(node.parent)
                jointList.append(f"P({node.value}|{concat})")
        return("⋅".join(jointList))


    def nodeFactors(self, node):
        nodee = [obj for obj in self.graph if obj.value == node][0]
        keys = self.genKeys(node)

        # Calculando el complemento de las probabilidades
        probs = nodee.probabilities
        allP = []
        for p in probs:
            allP.append(p)
            allP.append(1-p)
        
        keyC = {}
        if len(allP) != len(keys):
            raise ValueError("Hay un error")
        else:
            for i, k in enumerate(keys):
                if len(k) <= 2:
                    keyC[k] = allP[i]
                else:
                    keyC[k] = allP[i]
        return keyC


    def allFactors(self):
        factors = {}
        for node in self.graph:
            factors[node.value] = self.nodeFactors(node.value)
        return factors


    def mm(self, m1, m2):
        l_M1 = len(m1)
        l_M1_in, l_M2_in = len(m1[0]), len(m2[0])
        matrixR = []

        for rM1 in range(l_M1):
            new = []
            for cM2 in range(l_M2_in):
                new.append(sum(m1[rM1][rM2] * m2[rM2][cM2] for rM2 in range(l_M1_in)))
            matrixR = matrixR + [new]
        return matrixR

    
    

graph = Graph()
graph.addEdge("R", "A")
graph.addEdge("T", "A")
graph.addEdge("A", "J")
graph.addEdge("A", "M")
graph.addEdge("J", None)
graph.addEdge("M", None)

graph.addProb("J", [0.001], {'P(+J|+A)': 0.01, 'P(+J|-A)': 0.01})
# graph.addProb("T", [0.002])
# graph.addProb("A", [0.95, 0.94, 0.29, 0.001])
# graph.addProb("J", [0.9, 0.05])
# graph.addProb("M", [0.7, 0.01])

# print(graph.allFactors())
# print(graph.genKeys("A"))

# for j in graph.graph:
#     print("val: ", j.value, "probs: ", j.probabilities)

# for j in graph.graph:
#     print("val: ", j.value, "dep: ", j.dependencies, "parent: ", j.parent)


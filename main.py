import math
import itertools


class nodo():
    def __init__(self, value, dependencies, parent, probabilities):
        self.value = value
        self.parent = parent
        self.dependencies = dependencies
        self.probabilities = probabilities


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


    def cKeys(self, dictt, listt):
        for k in dictt:
            if k not in listt:
                return False
        return True


    def addProb(self, node, probD):
        nObj = [obj for obj in self.graph if obj.value == node]
        parent_s = len(nObj[0].parent)
        accepted = [x for x in self.genKeys(node) if not x.startswith('P(-')]
        
        if len(probD) != math.pow(2, parent_s):
             raise ValueError("Cantidad incorrecta de probabilidades")
        elif not self.cKeys(probD, accepted):
            raise ValueError("Llave(s) no permitidas")  
        elif not all(0 <= i <= 1 for i in probD.values()):
             raise ValueError("Las números deben encontrarse en un rango de 0 y 1")
        else:
            keysOrder = [x for x in self.genKeys(node) if not x.startswith('P(-')]
            probs = {k: probD[k] for k in keysOrder if k in probD}
            nObj[0].probabilities = probs


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
        keysOrder = [x for x in self.genKeys(node) if not x.startswith('P(-')]
        nP = nodee.probabilities
        probs = {k: nP[k] for k in keysOrder if k in nP}

        allP = []
        for p in probs:
            allP.append(probs[p])
            allP.append(1-(probs[p]))
        
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


    def allHaveValue(self):
        for obj in self.graph:
            if obj.value is None:
                return False
        return True


    def allHaveProbability(self):
        for obj in self.graph:
            if obj.probabilities is None:
                return False
        return True


    def correctQuantProbs(self):
        for obj in self.graph:
            nObj = [n for n in self.graph if n.value == obj.value][0]
            parent_s = len(nObj.parent)

            if len(obj.probabilities) != math.pow(2, parent_s):
                return False
        return True
    

    def described(self):
        allValue = self.allHaveValue()
        allProbability = self.allHaveProbability()
        correctProbsQuantity = self.correctQuantProbs()
        connections = self.checkConections()

        if(allValue and allProbability and correctProbsQuantity and connections):
            return True
        else:
            return False


    
    

graph = Graph()
graph.addEdge("R", "A")
graph.addEdge("T", "A")
graph.addEdge("A", "J")
graph.addEdge("A", "M")
graph.addEdge("J", None)
graph.addEdge("M", None)

# print(graph.nodeFactors("J"))
graph.addProb("R", {'P(+R)': 0.001})
graph.addProb("T", {'P(+T)': 0.002})
graph.addProb("A", {'P(+A|+R+T)': 0.95, 'P(+A|+R-T)': 0.94, 'P(+A|-R+T)': 0.29, 'P(+A|-R-T)': 0.001})
graph.addProb("J", {'P(+J|-A)': 0.05, 'P(+J|+A)': 0.9})
graph.addProb("M", {'P(+M|+A)': 0.7, 'P(+M|-A)': 0.01})

print(graph.described())
# print(graph.genKeys("A"))

# for j in graph.graph:
#     print("val: ", j.value, "probs: ", j.probabilities)

# for j in graph.graph:
#     print("val: ", j.value, "dep: ", j.dependencies, "parent: ", j.parent)


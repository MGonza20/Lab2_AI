

class nodo():
    def __init__(self, value, dependencies, parent, probabilities):
        self.value = value
        self.parent = parent
        self.dependencies = dependencies
        self.probabilities = probabilities
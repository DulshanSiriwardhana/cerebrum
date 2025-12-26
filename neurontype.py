class NeuronType():
    def __init__(self, activation, myelination):
        self.myelination = myelination
        self.activation = activation
        
    def getType(self):
        return {
            "activation": self.activation,
            "myelination": self.myelination,
        }
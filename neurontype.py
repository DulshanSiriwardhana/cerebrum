class NeuronType():
    def __init__(self, function, structure, signal, myelination, special):
        self.function = function
        self.structure = structure
        self.signal = signal
        self.myelination = myelination
        self.special = special
        
    def getType(self):
        return {
            "function": self.function,
            "structure": self.structure,
            "signal": self.signal,
            "myelination": self.myelination,
            "special": self.special
        }
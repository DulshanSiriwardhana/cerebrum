import cell as c
import neurontype as nt

neuronType = nt.NeuronType("Interneurons", "Multipolar", "Excitatory", "Myelinated", "Mirror")

cell1 = c.Cell(neuronType, [])

print(cell1.details().type.getType().function)
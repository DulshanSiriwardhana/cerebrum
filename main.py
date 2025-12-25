import cell as c
import neurontype as nt

neuronType = nt.NeuronType("Interneurons", "Multipolar", "Excitatory", "Myelinated", "Mirror")

cell1 = c.Cell(neuronType, [])
cell2 = c.Cell(neuronType, [])
cell3 = c.Cell(neuronType, [])
cell4 = c.Cell(neuronType, [])
cell5 = c.Cell(neuronType, [])

print(cell1.details())
print(cell2.details())
print(cell3.details())
print(cell4.details())
print(cell5.details())
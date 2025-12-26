import cell as c
import neurontype as nt

neuronType = nt.NeuronType("Interneurons", "Multipolar", "Excitatory", "Myelinated", "Mirror")

cell1 = c.Cell(neuronType, [])
cell2 = c.Cell(neuronType, [cell1])
cell3 = c.Cell(neuronType, [cell1, cell2])
cell4 = c.Cell(neuronType, [cell2])
cell5 = c.Cell(neuronType, [cell1, cell2, cell3, cell4])

cell5.fire(1)
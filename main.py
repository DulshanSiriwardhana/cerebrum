import cell as c
import neurontype as nt

neuronType = nt.NeuronType("Interneurons", "Multipolar", "Excitatory", "Myelinated", "Mirror")

cell1 = c.Cell(neuronType, [])
cell2 = c.Cell(neuronType, [])
cell3 = c.Cell(neuronType, [])
cell4 = c.Cell(neuronType, [])
cell5 = c.Cell(neuronType, [])

print(cell1.details().type.getType().function)
print(cell1.cell_id)
print(cell2.cell_id)
print(cell3.cell_id)
print(cell4.cell_id)
print(cell5.cell_id)
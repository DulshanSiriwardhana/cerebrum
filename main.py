import cell as c
import neurontype as nt

neuronType1 = nt.NeuronType("normal", "Myelinated")
neuronType2 = nt.NeuronType("sin", "Myelinated")
neuronType3 = nt.NeuronType("piStep", "Unmyelinated")
neuronType4 = nt.NeuronType("exp", "Unmyelinated")

cell1 = c.Cell(neuronType1, [], 1)
cell2 = c.Cell(neuronType2, [cell1], 2)
cell3 = c.Cell(neuronType3, [cell1, cell2], 3)
cell4 = c.Cell(neuronType3, [cell2], 4)
cell5 = c.Cell(neuronType4, [cell1, cell2, cell3, cell4], 5)

cell5.fire(1)
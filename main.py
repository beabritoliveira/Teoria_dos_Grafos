from arvGeradMinim import avgMin
from listaAdjacencia import listaAdjacencia
from menorCaminho import cMinimo

#QUESTAO 2
infin = float("inf") #colocando infinito no que não se tem caminho
M = [[99, 3, 5, 99, 8, 1, 99, 99],
     [3, 99, 2, 99, 99, 99, 1, 99],
     [5, 2, 99, 1, 99, 99, 99, 2],
     [99, 99, 1, 99, 4, 99, 99, 99],
     [8, 99, 99, 4, 99, 6, 99, 1],
     [1, 99, 99, 99, 6, 99, 5, 99],
     [99, 1, 99, 99, 99, 5, 99, 1],
     [99, 99, 2, 99, 1, 99, 1, 99]]

m = (cMinimo(M, 3, 6))
print(m[0])
print(m[1])
print()

#M = [[99, 2, 99, 99, 3, 2, 99],
#     [99, 99, 1, 99, 99, 99, 99],
#     [99, 99, 99, 1, 99, 99, 99],
#     [99, 99, 99, 99, 1, 99, 1],
#     [99, 99, 1, 99, 99, 1, 2],
#     [99, 99, 99, 99, 99, 99, 3],
#     [99, 99, 99, 99, 99, 99, 99]]

#print((cMinimo(M, 1, 7)))
#print((cMinimo(M, 3, 1)))

#QUESTÂO 3

M = [[99, 4, 99, 3, 4, 99],
     [4, 99, 8, 99, 9, 5],
     [99, 8, 99, 9, 3, 2],
     [3, 99, 9, 99, 99, 7],
     [4, 9, 3, 99, 99, 2],
     [99, 5, 2, 7, 2, 99]]

print(avgMin(M))

# Questão 4 a 6
M = [[99, 1, 99, 4, 99], #X
     [1, 99, 3, 1, 5], #1
     [99, 3, 99, 2, 2], #2
     [4, 1, 2, 99, 3], #3
     [99, 5, 2, 3, 99]] #Y

m = listaAdjacencia(M)
print(m[0])
print(m[1])
print(m[2])
print(m[3])
print(m[4])

# declarando uma matriz de adjacencia (YxY)
from menorCaminho import cMinimo


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

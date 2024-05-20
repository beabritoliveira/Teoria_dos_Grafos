def listaAdjacencia(matriz):
  tam = len(matriz)
  lista = [[0 for i in range(tam + 1)] for _ in range(tam)]
  for g in range(tam):
    lista[g][0] = g
  z = 0
  count = 1
  #for x in range(1, tam +1):
  while (z < tam):
    count = 1
    for x in range(0, tam):
      if (matriz[z][x] != 99):
        lista[z][count] = x
        count += 1
    z = z + 1
  return lista

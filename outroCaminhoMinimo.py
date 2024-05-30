def outroCaminho(matriz, Xvalue):
  tam = len(matriz)
  Xvalue = Xvalue 
  vertices = []
  distancia = []
  antescessor =[]
  #Inicialização da tabela
  for p in range(tam):
    vertices.append(p)
    distancia.append(matriz[Xvalue][p])
    antescessor.append(Xvalue) 
  distancia[Xvalue] = 0
  antescessor[Xvalue] = None
  for x in range(0, tam):
    for atual in vertices:
      for par in vertices:
        if(matriz[par][atual] != 99 and atual != Xvalue):
          vizinho = par
          if (matriz[vizinho][atual] + distancia[vizinho] < distancia[atual]):
            distancia[atual] = matriz[vizinho][atual] + distancia[vizinho]
            antescessor[atual] = par
  
  print(vertices)
  print(distancia)
  print(antescessor)
  return True

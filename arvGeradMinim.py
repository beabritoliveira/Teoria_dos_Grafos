def avgMin(matriz):
  #local de partida => Linha 0 = A 
  custoMinimo = 0
  IN = [0]
  menor = float("inf")
  tamMatriz = len(matriz)
  elem = 0
  for _ in range(tamMatriz -1):
    tamIN = len(IN)
    menor = float("inf")
    for g in range(tamMatriz):
      if(g in IN):
        for h in range(tamMatriz):
          if(not (h in IN)):
            if(menor > matriz[g][h]):
              menor =  matriz[g][h]
              elem = h
    print(menor)
    print(elem)
    print()
    custoMinimo += menor
    IN.append(elem)
    print(custoMinimo)
    print()
  return menor, IN, custoMinimo

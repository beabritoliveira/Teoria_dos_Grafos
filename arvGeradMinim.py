def avgMin(matriz):
  #local de partida => Linha 0 = A 
  custoMinimo = 0
  IN = [0]
  paresOrdenados = []
  menor = float("inf")
  tamMatriz = len(matriz)
  elem = 0
  deriv = 0
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
              deriv = g
    custoMinimo += menor
    IN.append(elem)
    paresOrdenados.append([deriv,elem])
    
  return IN, custoMinimo, paresOrdenados

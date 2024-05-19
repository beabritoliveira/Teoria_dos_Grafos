def cMinimo(matriz , Xvalue, Y):
  tam = len(matriz)
  Xvalue = Xvalue - 1
  Y = Y -1
  forceBreak = len(matriz)
  compArray = [ [ i for i in range(tam)] for _ in range(3)]
  #SETAR VALORES INICIAIS NA TABELA (distância e posição)
  for k in range(tam):
    if (k == Xvalue):
      compArray[2][k] = 90
    else : 
      compArray[2][k] = Xvalue

  # compArray[0][k] => NÃO ALTERA
  for q in range(tam):
    compArray[1][q] = matriz[Xvalue][q]
    if(q == Xvalue):
      compArray[1][q] = 0

  #print(compArray)
  IN = [Xvalue]
  maiorValor = 0
  indice = Xvalue
  while(IN[len(IN)-1] != Y):
    if(forceBreak == 0):
      return "Não há caminho entre esses vertices"
    forceBreak -= 1
    #ACHANDO VALORES POSIVEIS DE DISTÂNCIA
    conj = [] # guarda os possiveis valores
    ind= [] #guarda os indices dos possiveis valores
    for m in range(tam):
      if(compArray[1][m] > maiorValor and compArray[1][m] != 99 and compArray[1][m] >= compArray[1][indice]):
          if(not (m in IN)):
            conj.append(compArray[1][m])
            ind.append(m)
    menorValor = 90
    tamConjunto = len(conj)
    
    #Achando o menor valor
    for z in range(tamConjunto):
      if(conj[z] < menorValor):
        menorValor = conj[z]
        indice = ind[z]
    IN.append(indice)

    if(indice == Y):
      break
    #Achando a posição do menor valor
    for x in range(tam):
      novo = min(compArray[1][x], menorValor +  matriz[indice][x])
      if (compArray[1][x] != novo):
        compArray[2][x] = indice
        compArray[1][x] = novo
    
  index = Y
  ordemIN = [Y]
  #percorrendo IN para achar o real valor de IN
  while(index != Xvalue):
    index = compArray[2][index] 
    ordemIN.append(index)
  
  IN = []
  distancia = compArray[1][Y]
  #valores finais no IN
  for g in range(len(ordemIN)-1,-1,-1):
    IN.append(ordemIN[g])
  
  return IN, distancia

#compArray[0] => defini a posiçaõ da matriz
#compArray[1] => defini a distância entre os elementos
#compArray[2] => defini o seu predescessor no caminho

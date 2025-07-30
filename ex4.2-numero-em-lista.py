def numeroDeItens(lista):
  if lista == []:
    return 0
  return 1 + numeroDeItens(lista[1:])

print(numeroDeItens([0,1,2,3,4,5]))
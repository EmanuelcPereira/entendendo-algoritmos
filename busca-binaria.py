def buscaBinaria(lista, item):
  baixo = 0
  alto = len(lista) - 1

  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    if chute == item:
      return meio
    if chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  return None

lista = [1,2,5,7,11,17,21,27,34,59,61]
item = 2

print(buscaBinaria(lista, item))
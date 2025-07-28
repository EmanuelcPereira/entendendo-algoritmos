def buscaMenor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacaoSelecao(arr):
  novoArray = []
  for i in range(len(arr)):
    menor = buscaMenor(arr)
    novoArray.append(arr.pop(menor))
  return novoArray


print(ordenacaoSelecao([5,1,7,13,2,11,0]))

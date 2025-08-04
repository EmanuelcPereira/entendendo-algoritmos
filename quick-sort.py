def quickSort(array):
  if len(array) < 2:
    return array
  else:
    pivo = array[0]
    menor = [i for i in array[1:] if i <= pivo]
    maior = [i for i in array[1:] if i > pivo]
    return quickSort(menor) + [pivo] + quickSort(maior)

print(quickSort([10,30,2,4,38,28,1]))
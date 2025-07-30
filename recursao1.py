def soma(array):
  if array == []:
    return 0
  return array[0] + soma(array[1:])


print(soma([2,4,6]))
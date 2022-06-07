def decToBin(decimal):
  binario = ''	
  while decimal > 0:
    binario += str(decimal%2)
    decimal //= 2
  return binario[::-1]
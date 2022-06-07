def decToBin(decimal):
  binario = ''	
  while decimal > 0:
    binario += str(decimal%2)
    decimal //= 2
  return binario[::-1]

print("\n[DECIMAL -> BINÁRIO]")
decimal = int(input("Digite um número: "))
print(f"\n{decimal}₍₁₀₎ = {decToBin(decimal)}₍₂₎")
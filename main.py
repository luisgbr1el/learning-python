from functions.fatorial import fatorial
from functions.fibonacci import fibonacci
from functions.mmc import mmc
from functions.decToBin import decToBin

print("\n[MENU]")
print("1 - FATORIAL")
print("2 - FIBONACCI")
print("3 - MMC")
print("4 - DECIMAL PARA BINÁRIO")

choose = int(input("\nEscolha uma opção: "))

if choose == 1:
  print("\n[FATORIAL]")
  number = int(input("Digite um número: "))
  print(f"\n{number}! = {fatorial(number)}")
  
elif choose == 2:
  print("\n[FIBONACCI]")
  pos = int(input("Digite uma posição: "))
  print(f"\nA {pos}º posição do número de Fibonacci é {fibonacci(pos)}")
  
elif choose == 3: 
  print("\n[MMC]")
  n1 = int(input("Digite um número: "))
  n2 = int(input("Digite outro número: "))
  print(f"\nO MMC entre {n1} e {n2} é {int(mmc(n1, n2))}")
  
elif choose == 4:
  print("\n[DECIMAL -> BINÁRIO]")
  decimal = int(input("Digite um número: "))
  print(f"\n{decimal}₍₁₀₎ = {decToBin(decimal)}₍₂₎")
  
else:
  print("\n[Opção inválida!]")

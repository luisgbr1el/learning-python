def mmc(n1, n2):
  a = n1
  b = n2
  resto = 1

  while resto != 0:
    resto = a % b
    a = b
    b = resto

  return (n1 * n2) / a

print("\n[MMC]")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(f"\nO MMC entre {n1} e {n2} é {int(mmc(n1, n2))}")

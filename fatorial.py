def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)

print("\n[FATORIAL]")
number = int(input("Digite um número: "))
print(f"\n{number}! = {fatorial(number)}")

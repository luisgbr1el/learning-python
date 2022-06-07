def fibonacci(pos):
  i = 1
  last = 0

  while pos > 1:
    i += last
    last = i - last
    pos -= 1

  return i

print("\n[FIBONACCI]")
pos = int(input("Digite uma posição: "))
print(f"\nA {pos}º posição do número de Fibonacci é {fibonacci(pos)}")

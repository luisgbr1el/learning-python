print("[MENU]")
print("1 - FATORIAL")
print("2 - FIBONACCI")
print("3 - MMC")

choose = int(input("\nEscolha uma opção: "))

if choose == 1:
  __import__('fatorial')
elif choose == 2:
  __import__('fibonacci')
elif choose == 3:
  __import__('mmc')
else:
  print("\n[Opção inválida!]")

def mmc(n1, n2):
  a = n1
  b = n2
  resto = 1

  while resto != 0:
    resto = a % b
    a = b
    b = resto

  return (n1 * n2) / a
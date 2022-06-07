def fibonacci(pos):
  i = 1
  last = 0

  while pos > 1:
    i += last
    last = i - last
    pos -= 1

  return i
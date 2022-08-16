# This program finds the nth number in the Fibonacci sequence.

def fib_finder(n):
  fib = [0, 1]
  num = 0
  for i in range(n - 2):
    fib.append(fib[num] + fib[num + 1])
    num += 1

  return fib[n - 1]

print(fib_finder(6))

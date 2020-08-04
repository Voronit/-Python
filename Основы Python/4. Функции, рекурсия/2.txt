n = int(input("Enter number n: "))

def fib (n):
  if n == 2:
    return 1
  elif n == 1:
    return 1
  else:
    return fib(n-2) + fib(n-1)

print (fib(n))

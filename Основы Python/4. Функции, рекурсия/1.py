n = int(input("Enter number n: "))

def fact (n):
  res = 1
  for i in range(1, n + 1):
      res *= i
  return res

print(fact(n))

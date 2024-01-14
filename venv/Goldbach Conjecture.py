import math
def Prime(n):
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        return False
  return True

n = int(input())
for i in range(n):
    if Prime(i) and Prime(n-i):
        print(i,n-i)
        break

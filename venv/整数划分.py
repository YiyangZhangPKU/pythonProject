def divide(n,m):
    if n == 1 or m == 1:
        return 1
    elif n == m:
        return divide(n,n-1)+1
    elif m>n:
        return divide(n,n)
    else:
        return divide(n,m-1)+divide(n-m,m)

while True:
    try:
        n = int(input())
        print(divide(n,n))
    except EOFError:
        break

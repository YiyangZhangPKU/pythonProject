s =123 #算出来的值
a = 2
n = 7
slip = ""
out = ""
for i in range(n-1):
    slip += str(a)
    out += (slip+"+")
print(f"s={out}{slip}{a}={s}")


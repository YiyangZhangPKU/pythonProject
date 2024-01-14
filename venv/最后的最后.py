num,cycle = map(int,input().split())
nums = [i+1 for i in range(num)]
out = []
pointer = 0
for i in range(len(nums)):
    pointer= (pointer+cycle-1)%len(nums)
    out.append(nums.pop(pointer))
for i in range(len(out)-1):
    print(out[i], end=" ") if i != len(out) - 2 else print(out[i])


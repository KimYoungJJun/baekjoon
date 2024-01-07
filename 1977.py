import math
m = int(input())
n = int(input())

x = math.sqrt(m)
y = math.sqrt(n)
arr = []
for k in range(math.ceil(x), math.floor(y)+1):
    arr.append(k**2)
    
if arr:
    print(sum(arr),min(arr))
else:    
    print(-1)

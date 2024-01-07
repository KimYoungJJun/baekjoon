n = int(input())
price = []
name = []
for i in range(n):
    p = int(input())
    for j in range(p):
        value,name = input().split()
        value = int(value)
        if j == 0 or maxValue<value:
            maxValue = value
            maxName = name
    print(maxName)
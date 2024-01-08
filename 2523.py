n = int(input())
for i in range(1,2*n):
    for j in range(n):
        if (i<=n and j<i) or (i>n and i+j < 2*n):
            print("*", end = "")
    print()
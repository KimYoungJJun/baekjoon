n = int(input())
for i in range(1,2*n):
    for j in range(abs(n-i)):
        print(" ",end = "")
    if i<=n:
        for j in range(1,2*i):
            print("*",end = "")
    else:
        for j in range((2*n-1-i)*2+1):
            print("*",end = "")
    print()
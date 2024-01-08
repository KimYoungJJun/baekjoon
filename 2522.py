n = int(input())
for i in range(1,2*n):
    for j in range(abs(n-i)):
        print(" ",end = "")
    for j in range(abs(n-i),n):
        print("*",end = "")
    print()
n = int(input())
for i in range(1,2*n):
    for j in range(n-abs((n-i))):
        print("*", end = "")
    for j in range(abs(2*(n-i))):
        print(" ", end = "")
    for j in range(n-abs((n-i))):
        print("*", end = "")
    print()
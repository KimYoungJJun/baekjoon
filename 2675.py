n = int(input())

for i in range(n):
    line = list(map(str,input().split()))
    for k in range(len(line[1])):
        repeat = int(line[0])
        one = line[1][k]
        for j in range(0,repeat):
            print(one, end = "")
    print()
print()
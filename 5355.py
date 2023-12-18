
T = int(input())
for i in range(T):
    line = list(map(str,input().split()))
    answer = line[0]
    for j in range(len(line)):
        if j == 0:
            answer = float(line[j])
        elif line[j] == '@':
            answer *= 3
        elif line[j] == '%':
            answer += 5
        elif line[j] == '#':
            answer -= 7
    print("{:.2f}".format(answer))
    
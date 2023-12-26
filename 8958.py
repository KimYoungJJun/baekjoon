n = int(input())
for i in range(n):
    ox = list(map(str,input()))
    count = 0
    sum = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            count += 1
        elif ox[j] == 'X':
            count = 0
        sum += count
    print(sum)
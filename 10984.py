
T = int(input())
for i in range(T):
    N = int(input())
    sumcredit = 0
    sumscore = 0
    for j in range(N):
        credit, score = map(float,input().split())
        sumcredit += credit
        sumscore += (credit*score)
    sumscore /= sumcredit
    print(f"{int(sumcredit)} {round(sumscore,1)}")
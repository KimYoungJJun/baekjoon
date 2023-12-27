n = int(input())
yonsei_score = 0
korea_score = 0
for i in range(n):
    for j in range(9):
        yonsei, korea = map(int,input().split())
        yonsei_score+=yonsei
        korea_score+=korea
    if yonsei_score>korea_score:
        print("Yonsei")
    elif yonsei_score<korea_score:
        print("Korea")
    else:
        print("Draw")
        
    
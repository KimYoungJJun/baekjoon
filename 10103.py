n = int(input())
chang_score = 100
sang_score = 100

for i in range(n):
    chang, sang = map(int,input().split())
    
    if chang > sang:
        sang_score = sang_score - chang
    elif chang < sang:
        chang_score = chang_score - sang
    else:
        continue
    
    
print(chang_score)
print(sang_score)
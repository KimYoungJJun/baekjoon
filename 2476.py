n = int(input())
if n > 1000 or n < 2:
    exit()
arr = []
for i in range(n):
    a,b,c = map(int,input().split())
    if (a or b or c > 6) or (a or b or c < 1):
        exit()
    if a==b and b==c :
        arr.append(10000+a*1000)
    elif (a==b and a!=c):
        arr.append(1000+a*100)
    elif (a==c and a!=b):
        arr.append(1000+a*100)
    elif (b==c and a!=b):        
        arr.append(1000+a*100)
    elif a!=b and b!=c:
        arr.append(max(a,b,c)*100)
        
print(max(arr))
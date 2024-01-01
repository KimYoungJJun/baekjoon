'''n = int(input())
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
        
print(max(arr))'''
def same(a,b,c):
    if a==b and b==c:
        return 3
    elif (a==b and b!=c):
        return 2
    elif (a==c and a!=c):
        return 2
    elif (b==c and a!=b):
        return 2
    elif a!=b and b!=c:
        return 1
def number(a,b,c):
    if a==b:
        return a
    elif a==c:
        return a
    elif b==c:
        return b
        
result = []
n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if same(a,b,c)==3:
        result.append(10000 + 1000 * a)
    elif same(a,b,c)==2:
        result.append(1000 + number(a,b,c)*100)
    elif same(a,b,c)==1:
        result.append( max(a,b,c) * 100)
        
print(max(result))
        

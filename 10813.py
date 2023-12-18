
    
n,m = map(int,input().split())
l = []
for i in range(0,n+1):
    l.append(i)
for j in range(m):
    a,b = map(int,input().split())
    l[a],l[b] = l[b], l[a]
    
print(*l[1:])
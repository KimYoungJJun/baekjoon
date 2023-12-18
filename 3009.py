alist = []
blist = []
for i in range(0,3):
    a,b = list(map(int,input().split()))
    alist.append(a)
    blist.append(b)
    
    
for i in range(0,3):
    if alist.count(alist[i]) == 1:
        x4 = alist[i]
    if blist.count(blist[i]) == 1:
        y4 = blist[i]
        
print(x4,y4, end=" ")
print()
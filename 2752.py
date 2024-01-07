a,b,c = map(int,input().split())

lst = []
lst.append(a)
lst.append(b)
lst.append(c)

lst.sort()

for i in range(3):
    print(lst[i],end =" ")
    
print()
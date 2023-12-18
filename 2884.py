a,b = map(int,input().split())

if b<45:
    b+=15
    if a!=0:
        a-=1
    else:
        a=23
else:
    b-=45
    
print(a,b)
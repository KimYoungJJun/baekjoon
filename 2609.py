n,m = map(int,input().split())

if n<m:
    a = n
    b = m
else :
    a = m
    b = n
while a!=0 and b!=0:
    b = b % a
    if a > b :
        temp = a
        a = b
        b = temp
print(b)

print(int(n*m/b))
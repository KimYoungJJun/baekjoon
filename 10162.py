n = int(input())
A = 300
B = 60
C = 10
A_count = 0
B_count = 0
C_count = 0
if n>0 :
    while n >= 300:
        n = n - A
        A_count+=1
    while n >= 60:
        n = n - B
        B_count+=1
    while n >= 10:
        n = n - C
        C_count+=1
        
    if n%C != 0:
        print(-1)
        exit(0)
            
print(A_count,B_count,C_count, end=" ")
print()
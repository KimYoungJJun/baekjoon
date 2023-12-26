n = int(input())
arr = []
while n != -1:
    for i in range(1,n):
        if n%i==0:
            arr.append(i)
    
    if sum(arr) == n:
        print(f"{n} =", end=" ")
        for j in range(0,len(arr)-1):
            print(f"{arr[j]} +",end = " ")
        print(arr[-1])
    elif sum(arr)!= n:
        print(f"{n} is NOT perfect.")
        
    n = int(input())
    arr = []
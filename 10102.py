n = int(input())
arr = []
arr = list(map(str,input()))
A_count = 0
B_count = 0

for i in range(len(arr)):
    if arr[i] == 'A':
        A_count= A_count+1
    elif arr[i] == 'B':
        B_count = B_count+1
        
if A_count > B_count:
    print('A')
elif A_count < B_count:
    print('B')
else:
    print('Tie')
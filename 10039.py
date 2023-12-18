
arr = []
for i in range(0,5):
    arr.append( int(input()))
    
result = []
for i in arr:
    if i<40:
        result.append(40)
    else:
        result.append(i)
        
avg = sum(result)/5

print(int(avg))
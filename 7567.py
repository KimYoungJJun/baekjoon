dish = input()
result = []
result.append(10)
if(len(dish) > 50 or len(dish) < 3):
    exit(0)
for i in range(1,len(dish)):
    if dish[i] == dish[i-1]:
        result.append(5)
    elif dish[i] != dish[i-1]:
        result.append(10)

print(sum(result))
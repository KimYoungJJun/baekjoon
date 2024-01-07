allprice = int(input())
sumbook = 0
for i in range(9):
    price = int(input())
    sumbook += price
    
print(allprice-sumbook)
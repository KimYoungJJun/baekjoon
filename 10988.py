letter = input()

first = 0
last = len(letter)-1

while first < last:
    if letter[first] == letter[last]:
        first+=1
        last-=1
    else :
        break
    
if(first >= last):
    print(1)
else:
    print(0)
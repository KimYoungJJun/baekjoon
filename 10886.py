n = int(input())
arr = []
no_count=0
yes_count=0
for i in range(n):
    vote = int(input())
    if vote == 0:
        no_count+=1
    elif vote == 1:
        yes_count+=1
        
if no_count > yes_count :
    print("Junhee is not cute!")
elif no_count < yes_count:
    print("Junhee is cute!")
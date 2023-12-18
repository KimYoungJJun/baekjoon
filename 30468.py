STR,DEX,INT,LUK,n = map(int,input().split())

sum = (STR+DEX+INT+LUK)
if STR < 1 or DEX <1 or INT < 1 or LUK < 1 or n>100:
    exit(0)

if 4*n - sum > 0:
    print(4*n-sum)
else:
    print(0)
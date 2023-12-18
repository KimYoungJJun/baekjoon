A,B,C = map(int, input("정수 세 개 입력> ").split())

print( (A+B)%C)
print(((A%C) + (B%C))%C)
print(  (A*B)%C )
print( ((A%C) * (B%C))%C)

a = int(input())
b = int(input())

x = int(b/100)
y = int((b%100)/10)
z = int(b%10)

print(a*z)
print(a*y)
print(a*x)
print(a*b)
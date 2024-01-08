T = int(input())
for i in range(T):
    c,v = map(int,input().split())
    print(f"You get {int(c/v)} piece(s) and your dad gets {c%v} piece(s).")
hour,minute = map(int,input().split())
time = int(input())

if minute+time < 60:
    print(hour, minute+time)
else:
    hour += (minute+time)/60
    if hour>=24:
        hour %= 24
    minute = (minute+time)%60
    print(int(hour), minute)
score = input()

if score[0] == 'A':
    if score[1] == '+':
        result = 4.3
    elif score[1] == '0':
        result = 4.0
    elif score[1] == '-':
        result = 3.7
elif score[0] == 'B':
    if score[1] == '+':
        result = 3.3
    elif score[1] == '0':
        result = 3.0
    elif score[1] == '-':
        result = 2.7
elif score[0] == 'C':
    if score[1] == '+':
        result = 2.3
    elif score[1] == '0':
        result = 2.0
    elif score[1] == '-':
        result = 1.7
elif score[0] == 'D':
    if score[1] == '+':
        result = 1.3
    elif score[1] == '0':
        result = 1.0
    elif score[1] == '-':
        result = 0.7
elif score[0] == 'F':
    result = 0.0
    
print(result)
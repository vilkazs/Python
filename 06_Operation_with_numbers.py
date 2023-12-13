a = float(input())
b = float(input())
operand = str(input())

if operand == '+':
    print (a + b)
elif operand == '-':
    print (a - b)
elif operand == '/':
    if (b == 0):
        print ('Деление на 0!')
    else:
        print (a / b)
elif operand == '*':
    print (a * b)
elif operand == 'mod':
    if (b == 0):
        print ('Деление на 0!')
    else:
        print (a % b)
elif operand == 'pow':
    print (a ** b)
elif operand == 'div':
    if (b == 0):
        print ('Деление на 0!')
    else:
        print (a // b)
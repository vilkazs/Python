i = 0
while i < 5:
    a, b = input().split()	# split() разбивает строку на части по пробелам
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break # досрочно завершаем цикл
    print(a * b)
    i += 1
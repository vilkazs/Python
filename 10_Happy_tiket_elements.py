'''
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
Написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
'''

s = str(input())
sum1 = int(s[0]) + int(s[1]) + int(s[2])
sum2 = int(s[3]) + int(s[4]) + int(s[5])
if sum1 == sum2:
  print('Счастливый')
else:
  print('Обычный')
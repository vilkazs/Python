'''
Программа, считывающая с пользовательского ввода целое число n 
(неотрицательное), выводящее это число в консоль вместе с правильным образом 
изменённым словом "программист", для того, чтобы нормально общаться 
с людьми, например: 1 программист, 2 программиста, 5 программистов.
 
Проверьте, что  программа правильно обработает все случаи, как минимум до 1000 человек.
'''

n = int (input())
n0 = ' программист'
n1 = "ов"
n2 = "а"

if n>=0:
  if n==0:
    print(str(n) + n1)
  elif n % 100 >= 10 and n % 100 <= 20:
    print(str(n) + str(n0) + n1)
  elif n % 10 == 1:
    print(str(n) + str(n0))
  elif n % 10 >= 2 and n % 10 <= 4:
    print(str(n) + str(n0) + n2)
  else:
    print(str(n) + str(n0) + n1)
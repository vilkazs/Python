a = int(input())
b = int(input())
c = int(input())

max = a

# print(max, min, last)
if b > max:
    max = b
    if c > max:
        max = c
        print (max,'\n',a,'\n',b)
    else:
        if c > a:
            print (max,'\n',a,'\n',c)
        else:
            print (max,'\n',c,'\n',a)
elif c > max:
        max = c
        print (max,'\n',b,'\n',a)
else:
    if b > c:
        print (max,'\n',c,'\n',b)
    else:
        print (max, '\n',b,'\n',c)
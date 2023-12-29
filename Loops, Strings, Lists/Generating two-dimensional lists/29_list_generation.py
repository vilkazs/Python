n = 3
a = [[0] * n] * n
print(a)
a[0][0] = 5
print(a)

# Out:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[5, 0, 0], [5, 0, 0], [5, 0, 0]]


b = [[0] * n for i in range(n)]

c = [[0 for j in range(n)] for i in range(n)]
c[0][0] = 7
print(c)

# [[7, 0, 0], [0, 0, 0], [0, 0, 0]]
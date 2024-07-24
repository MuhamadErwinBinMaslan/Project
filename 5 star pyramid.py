n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

space = n - 1
star = 1
for i in range(1, n):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2

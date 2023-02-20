def squares(a, b):
    for i in range(a, b+1):
        yield i**2

for x in squares(1, 7):
    print(x)

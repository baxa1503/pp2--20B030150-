def square_generator(N):
    for i in range(N):
        yield i ** 2
for i in square_generator(7):
    print(i)

def natural_numbers():
    n = 1
    while True:
        yield n 
        n += 1

gen = natural_numbers()
for i in range(10):
    print(next(gen))
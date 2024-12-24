my_tuple = [10, 20, 30, 40, 50]
print(my_tuple[1])

y = list(my_tuple)
y[2] = "35"
my_tuple = tuple(y)

print(my_tuple)
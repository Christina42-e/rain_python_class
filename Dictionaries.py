my_dict = {
    'Name' : 'John',
    'Age' : 25,
    'City' : 'New york'

}

my_dict['job'] = 'Engineer'

my_dict.update({'Age': 26})

my_dict.pop('City')

x = my_dict.keys()
print(x)

x = my_dict.values()
print(x)

print(my_dict)
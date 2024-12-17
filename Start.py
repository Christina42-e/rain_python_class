print("Hello world")
if 5 > 2:
  print("Five is greater")
  print("2 is smaller")
  x=5
  y="hello world"
  print(id(x))
  print(id(y))#gives memory id of variables
  print(type(x))
  print(type(y)) #type check
  #python class notes

mail= """
Multi
line
string
"""
print(mail)
 
d=7.5
print(type(d))

e=int(d)
print(type(e))
a=3
b="2"
if a>int(b):
    print("a is greater")

    a = 1
    A = 4

    age = 8
    Age = 10 #different variables

    myObject = 5 # camel case
    MyObject = 5 # pascal case
    my_object= 5 # snake case

    x,y,z = "orange","Banana","mango"
    print(x)
    print(z)
    print(y)

    fruits = ["Orange","Banana","Mango","Pineapple"]
    x,y,z,a = fruits

    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not b)

    boy_age = 19
    boy_country = "Nepal"

    if boy_age > 18 and boy_country == "Nepal":
        print("Boy can give licence exam in Nepal")

first_number = float(input("Enter your first number:"))
second_number = float(input("enter your second number:"))

#first_number = int(first_number)
print("Addition = ", first_number + second_number)

first_number = float(input("Enter first number:"))
second_number = float(input("Enter second number"))

print("Substraction = ", first_number - second_number)

first_number = float(input("Enter first number:"))
second_number = float(input("Enter second number:"))

print("Multiplication = ", first_number * second_number)

first_number = float(input("Enter first number:"))
second_number = float(input("Enter second number:"))

print("Division = ", first_number / second_number)


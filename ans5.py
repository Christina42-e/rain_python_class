#Game Simple Number
a=int(input("Enter a number"))  # user input number in integer
b=a*2   # double
c=b+10
d=c/2
e=d-a
print(e)

user_input = float(input("Enter temperature in celsuis"))
x=((user_input*9/5)+32)
print("Temperature in fahrenheit =" ,x)

user_input = float(input("Enter the length value in meters"))
x=((user_input/1000))
print("Length value in kilometers =" ,x)

#unit converter

user_choices = input("""

1. KM to Miles
2. Miles to KM
3. Centimeter to Inch
4. Inch to Centimeter

""")

if user_choices ==  "1":
    user_input  = float(input("Enter KM"))
    result = user_input *    0.621371
    print(f"{user_input} KM = {resuult} Miles")

elif user_choices =="2":
    user_input = float(input("Enter Miles"))
    result =  user_input * 1.60934
    print(f"{user_input} Miles = {result} KM")

elif  user_choices == "3":
    user_choices == float(input("Enter Centimeter"))
    result = user_input * 0.393701
    print(f"{user_input} Centimeter = {result} Inch")

elif user_choices == "4":
    user_inpuut = float(input("Enter Inch"))
    result = user_input * 2.54
    print(f"{user_input} Inch = {result} Centimeter")

else:
    print("Invalid Input")

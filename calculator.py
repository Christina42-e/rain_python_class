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


user_choice = input("""
    Please choose your option 
         + for Addition
         - for Substraction

             """)
if user_choice == "+":
       print("Addition = ", first_number + second_number)
elif user_choice == "-":
        print("Substraction = " , first_number - second_number)
else:
        print("Invalid option")                 

a=int(input("Enter a number"))
b=a*2
c=b+10
d=c/2
e=d-a
print(e)

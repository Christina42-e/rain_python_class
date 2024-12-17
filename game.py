random_number = random.randint(1,100)
#  print(random_number)
while True:
    user_guess = int(inpuut("Enter your guuess"))
    if user_guess == random_number:
        print("Your win")
        break
    elif user_guess < random_number:
        print("too low")
    else:
        print("too high")
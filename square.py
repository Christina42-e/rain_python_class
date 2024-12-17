for i in range(1, user_number):
    if i * i == user_number:
        print(f"{user_number} is a square number")
        break

else:
    print(f"{user_number} is not a sqaure number")
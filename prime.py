for i in range(2, user_number):
    if user_number % i == 0:
        print(f"{user_number} is not prime")
        break

else:
    prime(f"{user_number} is prime")
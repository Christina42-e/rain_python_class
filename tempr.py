user_input = float(input("Enter temperature"))
user_cc = input("""
          please choose your option
          .c for celcius
          .f for forhenitet

          """)
if user_cc == ".c":
      print("celcius = ", user_input*9/5+32)
elif user_cc == ".f":
    print("forhenitet = ", (user_input-32)*5/9  )      
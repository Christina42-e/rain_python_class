def setup_mission():
    print("setting up  for the mission............")
    available_foods = [
    "apple",
    "banana",
    "watermelon",
    "chocolate",
    "water",
    "grapes",
    "pineapple",
    "cherry",
    "berries",
    "cupcakes",
    "pestries",
    "pizza",
    "burger",
]

    available_crews = int(input("Enter available crews"))
    print("setup completed.....")

    return available_crews, available_foods

#check battries over hundred
def get_charged_battries():
    batteries = [50,30,4,45,12,18,30]  ## battery basket
    minimum_battery_power = 20 ##battery use minimum 20% charge
    usable_battery_power = 0
    usable_battery_count = 0

    for battery in batteries: ## check every battery
      if battery > minimum_battery_power:  ##  check every battery IS OVERCHARGE 20% to use
       usable_battery_power += battery   ##if  yes use  power added
       usable_battery_count =  usable_battery_count  + 1  ##if yes use battery count add
      if usable_battery_power >= 100:
           return usable_battery_power, usable_battery_count

def decrypt_alien_message(alien_message):
    human_message =alien_message[::-1]   ##reverse string
    return human_message

def food_divide_equally(foods, crews_member):
    equally_foods = len(foods) // crews_member
    remaining_foods =  len(foods) % crews_member
    return equally_foods, remaining_foods

def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission............")

    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO MARS!!!!!!!!!!!!")

    print("Your battery is dead please!!!!!!! charge  the battery")
    battery_power, battery_count = get_charged_battries()

    print("Hurray!!!! Your battery is charged")

    print("Ooops!!! Alien has arrived saying:")
    print("rednerrus")

    decrypted_text = decrypt_alien_message("rednerrus")

    print(f"Alien is saying: {decrypted_text}")
    print("Alien has captured all astronauts")

    print("if astronut")

    print("Mission completed")

alien_attack_game()    
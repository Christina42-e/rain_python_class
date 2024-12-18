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


def alien_attack_game():
    print("Welcome to Alien Attack Game")
    print("Starting mission............")

    crews_number, foods = setup_mission()
    print(f"You have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO MARS!!!!!!!!!!!!")

    print("Your battery is dead please!!!!!!! charge  the battery")

    print("Mission completed")

alien_attack_game()    
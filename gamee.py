import time
import random
import pickle

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.consecutive_win_turns = 0

    def feed(self):
        self.hunger = min(100, self.hunger + 10)
        self.check_random_event()

    def play(self):
        self.happiness = min(100, self.happiness + 15)
        self.energy = max(0, self.energy - 10)
        self.check_random_event()

    def rest(self):
        self.energy = min(100, self.energy + 20)
        self.hunger = max(0, self.hunger - 5)
        self.check_random_event()

    def check_random_event(self):
        # Random event to boost happiness
        if random.randint(1, 5) == 1:
            self.happiness = min(100, self.happiness + 20)
            print(f"{self.name} found a toy! Happiness increased!")

    def check_status(self):
        print(f"\n{self.name}'s Current Stats:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

    def is_sick(self):
        return self.hunger == 0 or self.happiness == 0 or self.energy == 0

    def check_win(self):
        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            self.consecutive_win_turns += 1
            if self.consecutive_win_turns >= 3:
                print(f"\n{self.name} has become super happy and energetic! {self.name} wins!")
                return True
        else:
            self.consecutive_win_turns = 0
        return False

def save_game(pet):
    with open('pet_game_save.pkl', 'wb') as f:
        pickle.dump(pet, f)
    print("\nGame saved!")

def load_game():
    try:
        with open('pet_game_save.pkl', 'rb') as f:
            pet = pickle.load(f)
        print(f"\nWelcome back to {pet.name}'s game!")
        return pet
    except FileNotFoundError:
        print("\nNo saved game found. Starting a new game...")
        return None

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)
    print()

def main():
    print("Welcome to the Pet Care Game!")
    pet_name = input("Please name your pet: ")
    pet = Pet(pet_name)

    # Load game if previously saved
    if input("Do you want to load the previous game? (y/n): ").lower() == 'y':
        pet = load_game() or pet

    while True:
        if pet.is_sick():
            print(f"\n{pet.name} is sick and the game is over. Please try again!")
            break

        if pet.check_win():
            break

        pet.check_status()

        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Save and Quit")

        countdown_timer(10)  # countdown timer for user input
        action = input("\nChoose an action (1/2/3/4): ")

        if action == '1':
            pet.feed()
        elif action == '2':
            pet.play()
        elif action == '3':
            pet.rest()
        elif action == '4':
            save_game(pet)
            break
        else:
            print("\nInvalid option. Please choose again.")

if __name__ == "__main__":
    main()
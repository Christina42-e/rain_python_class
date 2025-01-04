import random
import time
import threading
import pickle

# Initialize pet attributes
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.turns_above_80 = 0

    def feed(self):
        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100

    def play(self):
        self.happiness += 10
        self.energy -= 10
        if self.happiness > 100:
            self.happiness = 100
        if self.energy < 0:
            self.energy = 0

    def rest(self):
        self.energy += 10
        self.hunger -= 5
        if self.energy > 100:
            self.energy = 100
        if self.hunger < 0:
            self.hunger = 0

    def check_status(self):
        return f"{self.name}'s Status:\nHunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}\n"

    def is_sick(self):
        return self.hunger == 0 or self.happiness == 0 or self.energy == 0

    def check_win(self):
        if self.hunger > 80 and self.happiness > 80 and self.energy > 80:
            self.turns_above_80 += 1
        else:
            self.turns_above_80 = 0
        return self.turns_above_80 >= 3


def random_event(pet):
    # Random event like finding a toy
    if random.random() < 0.2:  # 20% chance for a random event
        print(f"{pet.name} found a toy! Happiness +15!")
        pet.happiness += 15
        if pet.happiness > 100:
            pet.happiness = 100


def save_game(pet):
    with open("pet_game_save.pkl", "wb") as file:
        pickle.dump(pet, file)
    print("Game saved!")


def load_game():
    try:
        with open("pet_game_save.pkl", "rb") as file:
            pet = pickle.load(file)
        print(f"Game loaded! Welcome back, {pet.name}.")
        return pet
    except FileNotFoundError:
        print("No saved game found.")
        return None


# This function will allow the user to input their action within the given time frame
def prompt_input(prompt, timeout=8):
    print(f"{prompt} (You have {timeout} seconds to respond.)")
    
    user_input = []

    def get_input():
        user_input.append(input())

    # Start a thread to listen for user input
    thread = threading.Thread(target=get_input)
    thread.start()
    
    # Wait for the user input or the timeout
    thread.join(timeout)

    # If user input is received within time limit, return it; otherwise return 'rest'
    if user_input:
        return user_input[0].lower()
    else:
        print("\nTime's up! Defaulting to Rest action.")
        return 'rest'


def main():
    print("Welcome to the Pet Care Game!")
    name = input("What is the name of your pet? ")
    pet = Pet(name)

    # Load saved game or start fresh
    load_choice = input("Do you want to load your saved game? (y/n): ")
    if load_choice.lower() == 'y':
        pet = load_game()
        if pet is None:
            pet = Pet(name)
    else:
        print(f"Welcome, {pet.name}! Let's take care of your pet.")

    game_running = True
    while game_running:
        print(pet.check_status())
        random_event(pet)

        # Ask the user to choose an action or exit the game
        action = prompt_input("What would you like to do? (feed, play, rest, exit)", timeout=8)
        
        if action == 'feed':
            pet.feed()
        elif action == 'play':
            pet.play()
        elif action == 'rest':
            pet.rest()
        elif action == 'exit':
            print(f"You have exited the game. Goodbye, {pet.name}!")
            game_running = False
        else:
            print("Invalid choice, defaulting to Rest action.")
            pet.rest()

        if pet.is_sick():
            print(f"Your pet is sick! The game is over. {pet.name} failed to take care of themselves.")
            game_running = False
        elif pet.check_win():
            print(f"Congratulations! {pet.name} has become super happy and energetic! You've won the game!")
            game_running = False

        # Option to save the game after each turn
        save_choice = input("Do you want to save your game? (y/n): ")
        if save_choice.lower() == 'y':
            save_game(pet)


if __name__ == "__main__":
    main()

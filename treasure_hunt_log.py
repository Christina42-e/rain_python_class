import random
import datetime
import os
import time

INVENTORY_FILE = "Inventory.txt"

def save_to_file(filename, data,mode ="a"):
    """Save data to a file"""
    with open(filename,mode) as file:
        file.write(data + "\n")

def explore_location():
    """Explore a random location and find treasures."""
    locations = ["Mysterious Cave", "Haunted Forest","Deserted Beach","Ancient Ruins"]
    treasuures = ["Golden Crown","Silver Sword","Diamond Necklace","Ancient Artifact"]

    location = random.choice(locations)
    treasure = random.choice(treasures)

    print(f"\nExploring {location}......")
    time.sleep(2)
    print(f"You fouund a {treasure}!")

    save_to_file(INVENTORY_FILE,treasure)
    return treasure
    pass

def display_inventory():
    """Display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)

    else:
        print("\nNo entries in the leaderboard yet.")
    pass

def update_leaderboard(player_name,Score):
    """Update the leadership."""
    save_to_file

    pass

def treasure hunt():
    print("welcome to Treasure Hunt!")
    player_name = input("Enter your name:").strip()


    #Load inventory if it exits
    if os.path.exists(INVENTORY_FILE):
        print("\nResuming youur adventure........")

    else:
        print("\nStarting a new adventuure........")
        open(INVENTORY_FILE,"W").close()  #Create a empty inventory file

    score = 0

    while True:
        print("\nWhat would you like to do?")
        print("1.Explore a new location")
        print("2. view inventory")
        print("3. Quit and save progress")
        choice = input("Enter your choice (1/2/3):  ").strip() 

        if choice == "1":
            treasure = explore_location()
            score += 1
            print(f"You added {treasure} to your inventory!")

        elif choice == "2":
            display_inventory()

        elif choice == "3":
            print(f"\n Thanks for playing, {player_name}!")
            print(f"You collected")

def display_leaderboard():
    """Display the leaderboard"""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)

    else:
        print("\n No entries in the leaderboard  yet.")


def view_leaderboard():
    print("\n == Leaderboard ==")
    display_leaderboard()
    
def main():
    while True:
        print("\n == Treasure Hunt Menu == ")\
        print("1. Start/Resume  Game")
        print("2. View Leaderboard")
        print("3. Exit")
        choice  = input("Enter your choice (1/2/3):").strip()

        if choice == "1":
            treasure hunt()
        elif choice =="2":
            view leaderboard()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice Please try again")

    pass


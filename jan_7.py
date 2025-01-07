from collections import Counter

# Sample text
text = """
Python is an amazing programming language. Python is fun to learn and powerful to use.
"""
#split text into words 
words = text.lower().split()
word_count = Counter(words)

# Display word Frequencies
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

from queue import Queue
task_queue = Queue()

#create a task queue 
tasks = ["Task 1: Clean the room", "Task 2: Write Python code", "Task 3: Read a book"]
for task in tasks:
    task_queue.put(task)

# Process tasks
print("Processing Tasks:")
while not task_queue.empty():
    print(task_queue.get())

from collections import deque 
import random

deck = deque([f"{value} of {suit}" for value in
            ["2", "3", "4", "5", "6", "7", "8", "10", "jack", "Queen", "King", "Ace"]
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]])

random.shuffle(deck)

# players and their hands
player1 = []
player2 = []

#draw 3 cards for each player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())

#display players hand
print("Player 1's Hand:")
print(player1)
print("\nPlayer 2's Hand:")
print(player2)






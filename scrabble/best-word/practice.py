import os

srcPath = os.path.dirname(__file__)
textPath = os.path.join(srcPath, "alice.txt")

with open(textPath) as file:
    words = file.read().split() # Get words from file

letterPoints = {
    "a":  1,
    "b":  3,
    "c":  3,
    "d":  2,
    "e":  1,
    "f":  4,
    "g":  2,
    "h":  4,
    "i":  1,
    "j":  8,
    "k":  5,
    "l":  1,
    "m":  3,
    "n":  1,
    "o":  1,
    "p":  3,
    "q": 10,
    "r":  1,
    "s":  1,
    "t":  1,
    "u":  1,
    "v":  4,
    "w":  4,
    "x":  8,
    "y":  4,
    "z": 10,
}

bestWord = None # Keep track of the highest scoring word
bestScore = 0 # Keep track of the score of bestWord

# Find the word with the highest Scrabble score

for word in words:
    score = 0

    # Loop through each letter in the current word
    for letter in word:
        pass # Your code goes here!

    if score > bestScore:
        pass # Your code goes here!

print(bestWord)
import string
import random

# Receive guess from standard input 
def getGuess(preGuess, alphabet):
    while True:
        if (preGuess != []):
            print("You have previously guessed:", " ".join(preGuess))
            print("Letters remaining:", "".join(alphabet) + "\n")
        guess = str.lower(input("Please Enter the Letter you want to guess (A through Z): "))
        if (len(guess) != 1 or guess not in string.ascii_letters):
            print("\nPlease enter only one letter.\n")
        elif guess in preGuess:
            print("\nYou've already guessed that!\n")
        else:
            break
    return guess

# Find positions for right user guess
def find(word, rightletter):
    return [i for i, letter in enumerate(word) if letter == rightletter]

# Compare user guess with word 
def compare(guess, word, chance):
    rightLetter = ""
    for letter in word:
        if guess == letter:
            rightLetter = guess
            print("\nCorrect! You guessed a letter!")
            break
    if guess not in word:
        chance -= 1
        print("\nIncorrect!")
        if chance > 0:
            print("You have " + str(chance) + " chances left!")
    return rightLetter, chance

# Replace the empty list spot with the correct user guess
def fillWord(rightLetter, word, guessList):
    numLetter = 0
    positions = find(word, rightLetter)
    numLetter = len(positions)
    for position in positions: 
        guessList.pop(position)
        guessList.insert(position, rightLetter + " ")
    return guessList, numLetter

# Display win, lose, or number letters left and remaining list
def display(numWord, totalLetter, guessList, word, chance):
    print("".join(guessList))
    if (chance == 0):
        print("\nYOU LOST! The correct word is", str.upper(word) + "!")
    elif (numWord - totalLetter == 0):
        print("\nYOU WIN! The correct word is", str.upper(word) + "!")
    else:
        print("\nYou have", numWord - totalLetter,"Letters left to go!")

if __name__ == "__main__":
#Intro to Game
    print("Welcome to Andrew's Python Hangman Game!\n")

# Random word generation
    with open('words.txt', 'r') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        length = len(content)

# Choose random word from words.txt
    randInt = random.randint(1,length)
    word = str.lower(content[randInt])
    f.close()

# Intialize variables used in game
    totalLetter = 0
    chance = 6
    numWord = len(word)
    guessList = [' _ '] * numWord
    preGuess = []
    alphabet = []
    for letter in range(97,123):
        alphabet.append(chr(letter) + " ")

# Continue to loop through game until user guesses word correctly or has no more chances
    while (numWord != totalLetter and chance > 0):
        guess = getGuess(preGuess, alphabet)
        preGuess.append(guess)
        alphabet.remove(guess + " ")
        rightLetter, chance = compare(guess, word, chance)
        guessList, numLetter = fillWord(rightLetter, word, guessList)
        totalLetter += numLetter
        display(numWord, totalLetter, guessList, word, chance)
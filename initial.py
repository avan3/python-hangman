import string

#Intro to Game
print("Welcome to Andrew's Python Hangman Game!\n")

#Random word generation (in construction, work on it today)
import random

with open('words.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    length = len(content)
# you may also want to remove whitespace characters like `\n` at the end of each line
randInt = random.randint(1,length)
word = str.lower(content[randInt])
correct_word = list(word)
num_word = len(word)
alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter) + " ")

print("The word you are guessing has", num_word,"letters to guess!\n")

#Set variables to null value to be changed later in the program
num_letter = 0
chances = 0
correct_list = [' _ '] * num_word
previous_input = []

#Function for numbering the list for replacing the user input with the correct index
def find(list, letter):
    return [i for i, ltr in enumerate(list) if ltr == letter]

print("".join(correct_list) + "\n")

while (num_letter < num_word) and (chances < 10): #Win conditions
    user_guess = str.lower(input("Please Enter the Letter you want to guess (A through Z): "))
    if len(user_guess) == 1 and user_guess in string.ascii_letters: #user input can only be one character and a letter
        if user_guess + " " not in previous_input:
            alphabet.remove(user_guess + " ")
            previous_input.append(user_guess + " ") #checking if user input was previously inputted and added to a list
            print("You have previously guessed:", "".join(previous_input))
            for i in correct_word:  #Check each value in correct_word list
                if user_guess == i and user_guess not in correct_list:
                    position = find(correct_word, user_guess)
                    num_letter += len(position)
                    for j in position: #Replacing the empty list spot with the correct user input
                        correct_list.pop(j)
                        correct_list.insert(j, user_guess + " ")
                    if num_word - num_letter > 0:
                        print("\nYou got a letter! You have", num_word - num_letter, "letter(s) left to go!\n")
                        print("".join(correct_list), "\n") #Display list of correct input
                        print("Letters remaining:", "".join(alphabet), "\n")
                    elif num_word - num_letter == 0: #Win statement
                        print("\nYOU WIN! the correct word is", str.upper(word) + "!")
                        print("Correct letter(s) you entered:", "".join(correct_list))                        
                    break
                    
                elif user_guess not in correct_word: 
                    chances += 1 #Count every time they input wrong letter
                    if chances < 10: #10 chances = one time for head, body, 2 legs, 2 arms
                        print("\nWrong! You have", 10 - chances, "incorrect guesses left!\n")
                        print("".join(correct_list), "\n")
                        print("Letters remaining:", "".join(alphabet), "\n")
                    else: #End game if they input 10 times incorrectly
                        print("\nYou guessed too many times incorrectly!")
                        print("Sorry! YOU LOSE!")
                        print("The word was", content[randInt] + "!")
                    break
        elif user_guess + " " in previous_input:
            print("You have previously guessed:", "".join(previous_input))
            print("\nYou have guessed that already!\n") #Prompt user to choose another letter, but does not decrease chances for input
            print("".join(correct_list), "\n")
            print("Letters remaining:", "".join(alphabet), "\n")
    else:
        print("\nPlease enter only one letter.\n")
import random 
import sys

words = ['tiger','tree','underground','giraffe', 'chair'] 
def select_word(words):
    return random.choice(words) 
print(select_word(words))

remaining_attempts = 6 
guessed_letters = ""

def get_hangman_stage(remaining_attempts):
    max_attempts = 6
    
    stages = ["""
        -------
        |      |
        |
        |
        |
        |
        |
    ---------------
    """,  """
        ------
        |    |         
        |    O       
        |         
        |         
        |
        |
    ----------------
    """,  """
        ------
        |     |        
        |     O    
        |     |
        |     |
        |    /
        |
    ----------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |  // \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        | /// \\\ 
        |
    ------------
    """]
    return stages[max_attempts - remaining_attempts]
                          
def print_secret_word(secret_word):
    print(" _ " * len(secret_word)) 
    
print("welcome to the Hangman Game! Let's see if you can guess this word!\n")
secret_word = select_word(words) 
print(get_hangman_stage(remaining_attempts))
print_secret_word(secret_word)

def is_guess_in_secret_word(guess , secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letter are allowed: Unable to continue...") 
        sys.exit() 
    else:
        if guess in secret_word:
            return True 
        else: 
            return False
        
print("Welcome to Hangman! Let's see if you can guess this word!\n")
secret_word = select_word(words) 
guess = input('Guess a letter:') 
guess_in_secret_word = is_guess_in_secret_word(guess,secret_word) 

if guess_in_secret_word:
    if guess in guessed_letters:
        print('You have already guessed the letter {}'.format(guess)) 
    else:
        print('Yes! The letter {}  is part of the secret word'.format(guess))
        guessed_letters += guess 
else:
    print('No! The letter {} is not part of the secret word'.format(guess)) 
    remaining_attempts -= 1
print(get_hangman_stage(remaining_attempts)) 
print_secret_word(secret_word)


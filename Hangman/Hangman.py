import random

from words import words

import string

def choosing_valid_word(words):
    word = random.choice(words).upper()
    while "-" in words or " " in words:
       word = random.choice(words).upper()
    return word

def hangman():
    word = choosing_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    while len(word_letters) > 0:
        #letter used
        print("You have already used: ", " ".join(used_letter))
        
        # current words used
        word_list =[letter if letter in used_letter else "*" for letter in word]
        
        print("current word ", " ".join(word_list))
        
    #getting the user letter
        user_letter = input("What is your letter? ").upper()
        
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letter:
            print("You have already used that letter! Choose again!")
        else:
            print("Invalid input")
hangman()
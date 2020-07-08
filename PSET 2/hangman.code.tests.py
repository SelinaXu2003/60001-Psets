# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:05:04 2020

@author: selin
"""

#secret_word = "apple"
#letters_guessed = ["e", "i", "k", "p", "r", "s" ]

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for character in secret_word:
        if character not in letters_guessed:
            return False
    return True

#print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):

    '''

    secret_word: string, the word the user is guessing

    letters_guessed: list (of letters), which letters have been guessed so far

    returns: string, comprised of letters, underscores (_), and spaces that represents

      which letters in secret_word have been guessed so far.

    '''

    l = ['_ '] * len(secret_word)

    for i in range(len(secret_word)):

        for let in letters_guessed:

            if secret_word[i] == let:

                l[i] = let

    return ''.join(l)

#print(get_guessed_word(secret_word, letters_guessed))

import string
letters_guessed = ["e", "i", "k", "p", "r", "s"]
#print(letters_guessed)
#alphabet = list(string.ascii_lowercase)
#print(alphabet)
#for char in letters_guessed:
#    if char in alphabet:
#        alphabet.remove(char)
#print (alphabet)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in alphabet:
            alphabet.remove(char)
    return alphabet

#print(get_available_letters(letters_guessed))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    
    length_sw = len(secret_word)
    
    letters_guessed = []
    
    
    warnings_remaining = 3
    
    print("Welcome to Hangman")
    
    print("I am thinking of a world that is", length_sw, "letters long.")
    
    print("You have", guesses ,"guesses")
    
    print("Available letters are:", get_available_letters(letters_guessed))
    
    print("-------------")
    
    while True:
        
        users_guess = str.lower(input("Enter any letter:"))
        
        #If the ueser enter a word
        if len(users_guess) > 1:
            
            print("This is not a letter.")
            
            print("-------------")
            
            print(get_available_letters(letters_guessed))
            
            print("You have", guesses ,"guesses remaining.")
            
            continue
        
        #If the user enters a letter they have already entered
        if (users_guess in letters_guessed) and warnings_remaining >= 1:
            
            warnings_remaining -= 1
            
            letters_guessed.append(users_guess)
            
            print("Oops! You have already entered this letter. You have:", warnings_remaining, "left.")
            
            get_guessed_word(secret_word, letters_guessed)
                             
            print("-------------")
            
            print(get_available_letters(letters_guessed))
            
            print("You have", guesses ,"guesses remaining.")
        
        #If the user enters a symbol
        elif not str.isalpha(users_guess) and warnings_remaining >= 1:
            warnings_remaining -= 1
            
            letters_guessed.append(users_guess)
            
            print("Oops! You have entered an invalid character.You have:", warnings_remaining, "left.")
            
            get_guessed_word(secret_word, letters_guessed)
                             
            print("-------------")
            
            print(get_available_letters(letters_guessed))
            
            print("You have", guesses ,"guesses remaining.")
        
        #If the user enters a symbol and when the warnings reach 0
        elif not str.isalpha(users_guess) and warnings_remaining == 0:

            letters_guessed.append(users_guess)

            guesses = guesses - 1

            print('Oops! That is not a valid letter:', get_guessed_word(secret_word, letters_guessed))

            print('-------------')

            print('You have', guesses, 'guesses left.')

            print('Available letters:', get_available_letters(letters_guessed))

            if guesses == 0:

                print('-------------')

                print('Sorry, you ran out of guesses. The word was', secret_word)

                break
        
        #If the user enters a letter that they ahve already guessed and when the warnings reach 0
        elif (users_guess in letters_guessed) and warnings_remaining == 0:

            letters_guessed.append(users_guess)

            guesses = guesses - 1

            print('Oops! You\'ve already guessed that letter:', get_guessed_word(secret_word, letters_guessed))

            print('-------------')

            print('You have', guesses, 'guesses left.')

            print('Available letters:', get_available_letters(letters_guessed))

            if guesses == 0:

                print('-------------')

                print('Sorry, you ran out of guesses. The word was', secret_word)

                break
            
        # If the user guesses correctly
        elif users_guess in secret_word and users_guess not in letters_guessed:
            
            letters_guessed.append(users_guess)
            
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))

            print('-------------')

            print('You have', guesses, 'guesses left.')

            print('Available letters:', get_available_letters(letters_guessed))
        
        #If the users guesses wrong
        elif (users_guess not in secret_word)and (str.isalpha(users_guess)) and (users_guess not in letters_guessed):
        
            letters_guessed.append(users_guess)
            
            guesses -= 1
            
            print("Oops! This letter is not in the word.", get_guessed_word(secret_word, letters_guessed))
            
            print('-------------')
            
            if guesses > 1:
                
                print('You have', guesses, 'guesses left.')
                
                print('Available letters:', get_available_letters(letters_guessed))
            
            else:
                
                print("Uh-oh. You are out of guesses.")
                
                print("The word was:", secret_word)
                
                break
        #If the user correctly guesses the word
        if is_word_guessed(secret_word, letters_guessed):
            
            print('-------------')
            
            print('Congratulations, you won! The secret word was:', secret_word)
            
            break


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = "apple"
    hangman(secret_word)
        
        
    
        
        

    
    



    
        
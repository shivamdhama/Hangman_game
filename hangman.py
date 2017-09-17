# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist
#Exit of LoadWord


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
    #-----------------------------------------------------------End of Function--------------------------------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    #s = ''
    '''count = 0
    for s in secretWord:
        if s in lettersGuessed:
            count+=1
    if count == len(secretWord):
        return True'''
    #Aleternate code for this func. ...one line code..
    return True if all(letter in lettersGuessed for letter in secretWord)else False
    
    #-------------------------End of Function-------------------------------------------------


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
      return example: '_ p p _ _'
    '''
    # FILL IN YOUR CODE HERE...
    str_final=''
    c=''
    for c in secretWord:
        if c in lettersGuessed:
            str_final+= (c+ ' ')
            
        else:
            str_final+= '__ '
    return str_final.rstrip()
    #-------------------------End of Function-----------------------
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    original_list=list(string.ascii_lowercase)  #printing alphabets 
    new_list = [item for item in original_list if item not in lettersGuessed] #update let list
    return " ".join(new_list)
    #-------------------------End of Function-------------------------------

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    guess = ''                          #user guessed the letters one by one
    a = len(secretWord)
    guess_length = len(secretWord) + 5    
    print ("Welcome to Hangman Game....lets play")
    print ("length of Secret word is: ",a)
    
    while guess_length > 0:
        if (True == isWordGuessed(secretWord, lettersGuessed)):
            print("Congratulation!!....you win..")
            break        
        print ('-----------------------*********------------------------')
        print ("your guess limit is: ", guess_length)
        guess = input("Enter a letter :- ")
        if guess in secretWord:
            lettersGuessed.append(str(guess))
            print (getGuessedWord(secretWord, lettersGuessed))
            print (getAvailableLetters(lettersGuessed))
        else:
            lettersGuessed.append(str(guess))
            print (getGuessedWord(secretWord, lettersGuessed))
            print (getAvailableLetters(lettersGuessed))
          
        guess_length-= 1
        print ("you have used..")
        print (" ".join(lettersGuessed)) 

    if guess_length == 0:
        print ("You did\'t get secretword....SO,You lose")
        print ("Secret word is: ",secretWord)
 

#---------------------------------End of Hangman function..------------------------------


#secretWord="dhama"
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

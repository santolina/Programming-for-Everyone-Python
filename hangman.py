# Hangman game, which is an example implementation to solve "week3 Problem set 3" 
# of MITx: 6.00.1x Introduction to Computer Science and Programming Using Python on edX.
#
# Here is a link to the course: https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/
#
# It is strongly recommeded to solve problems for yourself.
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt" # it should be modified for each your env.

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    numSuccess  = 0
    for letter in lettersGuessed:
        if letter in secretWord:
            numSuccess += 1
    
    if numSuccess == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
#    print "secretWord: ", secretWord
#    print "letterGuessed: ", lettersGuessed
    tmp = secretWord[:]
    secretWordList = list(tmp)
    guessedWord = []
    
#    print guessedWord, secretWordList, guessedWordMarker
    for letter in secretWordList:
        #print letter
        if letter in lettersGuessed:
            guessedWord.append(letter)
        else:
            guessedWord.append("_ ")
            
#    print str(guessedWord)
    out = ""
    for w in guessedWord:
        out = out + w
 #   print out
    return out

# test
#print getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']) 
# '_ pp_ e'

#print getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
# 'durian'

#print getGuessedWord('banana', ['s', 'w', 'f', 'n', 'o', 'i', 'u', 'x', 'l', 'z'])
# '_ _ n_ n_ '

#print getGuessedWord('lettuce', ['a', 'o', 'm', 's', 'f', 'k', 't', 'j', 'p', 'l']) 
# 'l_ tt_ _ _ '

#print getGuessedWord('carrot', [])
# '_ _ _ _ _ _ '

#print getGuessedWord('grapefruit', ['u', 'l', 'h', 'p', 'z', 'e', 'f', 's', 'v', 'b'])
# '_ _ _ pef_ u_ _ '


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphaList = list(alphabets)
    lettersGuessedList = list(lettersGuessed)
    out = ""
    #print "alphaList: ", alphaList
    #print "letterGuessedList: ", lettersGuessedList
    for letter in alphaList:
        if letter not in lettersGuessedList:
            #print "letter %s is not in %s" % (letter, lettersGuessedList)
            out = out + letter 
    #print "after: ", out
    
    return out
  
#print "abc", getAvailableLetters("abc")      
#print "cdf", getAvailableLetters("cdf")      
#print "xyz", getAvailableLetters("xyz")      
#print "az", getAvailableLetters("xyz")   

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
    # define  
    remNumTry = 8
    welcome = "Welcome to the game, Hangman!"
    boader = "-------------"
    availLetters = getAvailableLetters("")
    # start
    print (welcome)
    print ("I am thiking of a word that is %d letters long" % (len(secretWord)))
    lettersGuessed = []
    guessedWords = getGuessedWord(secretWord, lettersGuessed)
    while remNumTry>0:
        letterGuessedstr=""
        for w in lettersGuessed:
            letterGuessedstr = letterGuessedstr + w
        availLetters = getAvailableLetters(letterGuessedstr)
        print boader
        print "You have %d geusses left." % (remNumTry)
        print "Available letters: " + availLetters
        inp = raw_input("Please guess a letter: ")
        inp = inp.lower()
        
        if len(inp)!=1:
            continue
        
        # check duplicated input
        if inp in lettersGuessed:
            guessedWords = getGuessedWord(secretWord, lettersGuessed)
            print "Oops! You've already guessed that letter: " + guessedWords
            continue
        else:
            lettersGuessed.append(inp)
        
        # getGuessedWord(secretWord, lettersGuessed)
        guessedWords = getGuessedWord(secretWord, lettersGuessed)
        if inp not in secretWord:
           print "Oops! That letter is not in my word: " + guessedWords
           remNumTry  = remNumTry - 1
           continue
                                                                 
        # check guessed word is equal to answered
        elif isWordGuessed(secretWord, guessedWords):
           print "Good guess: " +  guessedWords
           print boader
           print "Congratulations, you won!"
           break
        else:
           print "Good guess: " +  guessedWords
            
    if remNumTry <= 0:
        print boader       
        print "Sorry, you ran out of guesses. The word was else."

# Main 
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

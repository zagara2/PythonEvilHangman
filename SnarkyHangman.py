'''
Created on Apr 14, 2016

@author: Mickey
'''
import random

DEBUG = False

def fileToStringList(filename):
    """
    filename is a file of strings, 
    returns a list of strings, each string represents
    one line from filename
    """
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist
    
def longestPossibleWord(lst):
    '''
    gets a list as a parameter, returns length of longest item in list
    '''
    itemLengths = [len(item) for item in lst]
    return max(itemLengths)    
     
def getPossibleWords(wordlist,length):
    """
    returns a list of words from wordlist having a 
    specified length 
    """
    wordlist = [item for item in wordlist if len(item)== length]
    return wordlist

def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(wordList)

def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as word
    '''
    return ['_']*len(word)

def updateLetter(guessList,wordToGuess, letter):
    '''
    wordToGuess is the word the user is trying to guess.
    guessList is the word to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed. 
    
    This function modifies guessList to include letter in its proper locations if 
    letter is in wordToGuess.
    
    '''
    if letter.lower() in wordToGuess or letter.upper() in wordToGuess:
        print "You guessed a letter!"
        for x in range(0, len(guessList)):
            if wordToGuess[x] == letter.lower():
                guessList[x] = letter.lower()
            elif wordToGuess[x] == letter.upper():
                guessList[x] = letter.upper()
    else:
        print "That's a miss!"
    return guessList

def updateLetter2(guessList,wordToGuess, letter):
    '''
Same thing as updateLetter but doesn't have print statements to tell you if you guessed 
a letter or got a miss. Just modifies guessList to include letter in its proper locations if 
letter is in wordToGuess.
    
    '''
    
    if letter.lower() in wordToGuess or letter.upper() in wordToGuess:
        for x in range(0, len(guessList)):
            if wordToGuess[x] == letter.lower():
                guessList[x] = letter.lower()
            elif wordToGuess[x] == letter.upper():
                guessList[x] = letter.upper()
    return guessList

def checkForLetters(word, lettersGuessed):
    '''
    checks if any character in String lettersGuessed is in String word
    '''
    for ch in lettersGuessed:
        if ch in word:
            return False
    return True

def checkIfMatch(word, guessList):
    '''
    for every item in list guessList that is not a blank (i.e. is a letter), checks 
    if that letter matches up with the letter at the corresponding index in String word
    '''
    for x in range(0, len(guessList)):
        if guessList[x] != "_":
            if word.count(guessList[x]) > guessList.count(guessList[x]):
                return False
            if word[x] != guessList[x]:
                return False
    return True
            




def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    if DEBUG == True: #play game in test mode
        #setup for game. correcting for faulty input
        try:
            guessLength = int(raw_input("how many letters in word to guess? Must be at least 3. "))
            if guessLength < 3:
                print "You entered a number less than 3. Word length will be set to 3."
                guessLength = 3
            allwords = fileToStringList("lowerwords.txt")
            longestLength = longestPossibleWord(allwords)
            if guessLength > longestLength:
                guessLength = longestLength
                print "That's too long. Word length will be set to longest possible length, which is", longestLength
        except: #assigns a random word length if user enters something non-numerical
            guessLength = random.randint(3,9)
            print "That doesn't seem like a number. Word length will be set to", guessLength
            
        try: 
            numberMissesAllowed = int(raw_input("how many misses allowed? "))
            if numberMissesAllowed <= 0:
                numberMissesAllowed = 1
                print "You can't start with that amount of misses. Number of misses will be set to 1."
        except: #assigns a random number of misses if user enters something non-numerical
            numberMissesAllowed = random.randint(3,15)
            print "That doesn't seem like a number. Number of misses allowed will be set to", numberMissesAllowed
        wordsOfLength = getPossibleWords(words,guessLength)
        #print wordsOfLength
        wordToGuess = random.choice(wordsOfLength)
        guessList = guessStart(wordToGuess)
        #print guessList
    
        
        # start the guessing
        misscount = 0
        lettersGuessed = ""
        correctGuesses= ""
        incorrectGuesses = "" 
        while True:
            if guessList.count('_') == 0:
                # all letters guessed
                break
            print
            print "guessed so far: ", displayGuess(guessList)
            print "letters already guessed: ", lettersGuessed
            print "number of misses left: ", numberMissesAllowed-misscount
            print "correct guesses: ", correctGuesses
            print "incorrect guesses: ", incorrectGuesses
            print "Secret word is: ", wordToGuess
            print
            guessDict = {}
            letter = raw_input("guess a letter: ")
            letter = letter.strip()
            if not letter.isalpha(): #correcting for non-alphabetical chars
                print "That's not a letter!"
                continue
            if len(letter)>1: #correcting for multiple letters guessed at once
                print "Please guess one letter at a time."
                continue
            if letter.lower() in lettersGuessed: #correcting for same letter guessed multiple times
                print "You guessed that letter already."
                continue
    
    
            for item in wordsOfLength:
                if checkIfMatch(item, guessList) and checkForLetters(item, incorrectGuesses):
                    guesslisttemp = guessList[:]
                    mykeyList = updateLetter2(guesslisttemp, item, letter)
                    mykey = displayGuess(mykeyList)
                    if mykey not in guessDict:
                        guessDict[mykey] = [item]
                    else:
                        guessDict[mykey].append(item)
            mylist = sorted([(len(v), k) for (k, v) in guessDict.items()])
            mylist.reverse()
            total = sum([len(v) for (k, v) in guessDict.items()])
            print "Dictionary of Categories and # words:"
            print mylist
            print "total possibilities left: ", total
            if mylist == []:
                updateLetter(guessList, wordToGuess, letter)
                lettersGuessed = lettersGuessed + letter.lower()
                lettersGuessed = ''.join(sorted(lettersGuessed))
                if letter.lower() in guessList:
                    correctGuesses = correctGuesses + letter.lower()
                    correctGuesses = ''.join(sorted(correctGuesses))
                else:
                    incorrectGuesses = incorrectGuesses + letter.lower()
                    incorrectGuesses = ''.join(sorted(incorrectGuesses))
                    misscount = misscount + 1
                if misscount == numberMissesAllowed: #user runs out of guesses
                    break
                continue
            targetKey = mylist[0][1]
            listofVals = guessDict[targetKey]
            wordToGuess = random.choice(listofVals)
       
                
            updateLetter(guessList, wordToGuess, letter)
            lettersGuessed = lettersGuessed + letter.lower()
            lettersGuessed = ''.join(sorted(lettersGuessed))
            if letter.lower() in guessList:
                correctGuesses = correctGuesses + letter.lower()
                correctGuesses = ''.join(sorted(correctGuesses))
            else:
                incorrectGuesses = incorrectGuesses + letter.lower()
                incorrectGuesses = ''.join(sorted(incorrectGuesses))
                misscount = misscount + 1
            if misscount == numberMissesAllowed: #user runs out of guesses
                break
         
        # game over
        if guessList.count('_') == 0:
            print
            print "You win. You guessed the word", wordToGuess
            print "number of misses left upon ending game:", numberMissesAllowed-misscount
            print "all letters guessed during game:", lettersGuessed
        else:
            print
            print "You lost, you ran out of guesses. Word was", wordToGuess
            print "number of misses left upon ending game:", numberMissesAllowed-misscount
            print "all letters guessed during game:", lettersGuessed
    
    else: #play in game mode
        #setup for game. correcting for faulty input
        try:
            guessLength = int(raw_input("how many letters in word to guess? Must be at least 3. "))
            if guessLength < 3:
                print "You entered a number less than 3. Word length will be set to 3."
                guessLength = 3
            allwords = fileToStringList("lowerwords.txt")
            longestLength = longestPossibleWord(allwords)
            if guessLength > longestLength:
                guessLength = longestLength
                print "That's too long. Word length will be set to longest possible length, which is", longestLength
        except: #assigns a random word length if user enters something non-numerical
            guessLength = random.randint(3,9)
            print "That doesn't seem like a number. Word length will be set to", guessLength
            
        try: 
            numberMissesAllowed = int(raw_input("how many misses allowed? "))
            if numberMissesAllowed <= 0:
                numberMissesAllowed = 1
                print "You can't start with that amount of misses. Number of misses will be set to 1."
        except: #assigns a random number of misses if user enters something non-numerical
            numberMissesAllowed = random.randint(3,15)
            print "That doesn't seem like a number. Number of misses allowed will be set to", numberMissesAllowed
        wordsOfLength = getPossibleWords(words,guessLength)
        #print wordsOfLength
        wordToGuess = random.choice(wordsOfLength)
        guessList = guessStart(wordToGuess)
        #print guessList
    
        
        # start the guessing
        misscount = 0
        lettersGuessed = ""
        correctGuesses= ""
        incorrectGuesses = "" 
        while True:
            if guessList.count('_') == 0:
                # all letters guessed
                break
            print
            print "guessed so far: ", displayGuess(guessList)
            print "letters already guessed: ", lettersGuessed
            print "number of misses left: ", numberMissesAllowed-misscount
            print
            guessDict = {}
            letter = raw_input("guess a letter: ")
            letter = letter.strip()
            if not letter.isalpha(): #correcting for non-alphabetical chars
                print "That's not a letter!"
                continue
            if len(letter)>1: #correcting for multiple letters guessed at once
                print "Please guess one letter at a time."
                continue
            if letter.lower() in lettersGuessed: #correcting for same letter guessed multiple times
                print "You guessed that letter already."
                continue
    
    
            for item in wordsOfLength:
                if checkIfMatch(item, guessList) and checkForLetters(item, incorrectGuesses):
                    guesslisttemp = guessList[:]
                    mykeyList = updateLetter2(guesslisttemp, item, letter)
                    mykey = displayGuess(mykeyList)
                    if mykey not in guessDict:
                        guessDict[mykey] = [item]
                    else:
                        guessDict[mykey].append(item)
            mylist = sorted([(len(v), k) for (k, v) in guessDict.items()])
            mylist.reverse()

            if mylist == []:
                updateLetter(guessList, wordToGuess, letter)
                lettersGuessed = lettersGuessed + letter.lower()
                lettersGuessed = ''.join(sorted(lettersGuessed))
                if letter.lower() in guessList:
                    correctGuesses = correctGuesses + letter.lower()
                    correctGuesses = ''.join(sorted(correctGuesses))
                else:
                    incorrectGuesses = incorrectGuesses + letter.lower()
                    incorrectGuesses = ''.join(sorted(incorrectGuesses))
                    misscount = misscount + 1
                if misscount == numberMissesAllowed: #user runs out of guesses
                    break
                continue
            targetKey = mylist[0][1]
            listofVals = guessDict[targetKey]
            wordToGuess = random.choice(listofVals)
       
                
            updateLetter(guessList, wordToGuess, letter)
            lettersGuessed = lettersGuessed + letter.lower()
            lettersGuessed = ''.join(sorted(lettersGuessed))
            if letter.lower() in guessList:
                correctGuesses = correctGuesses + letter.lower()
                correctGuesses = ''.join(sorted(correctGuesses))
            else:
                incorrectGuesses = incorrectGuesses + letter.lower()
                incorrectGuesses = ''.join(sorted(incorrectGuesses))
                misscount = misscount + 1
            if misscount == numberMissesAllowed: #user runs out of guesses
                break
         
        # game over
        if guessList.count('_') == 0:
            print
            print "You win. You guessed the word", wordToGuess
            print "number of misses left upon ending game:", numberMissesAllowed-misscount
            print "all letters guessed during game:", lettersGuessed
        else:
            print
            print "You lost, you ran out of guesses. Word was", wordToGuess
            print "number of misses left upon ending game:", numberMissesAllowed-misscount
            print "all letters guessed during game:", lettersGuessed
    


if __name__ == '__main__':
    words = fileToStringList('lowerwords.txt')
    print "game (g) or testing(t) mode?"
    
    mode = raw_input("g or t?: ")
    if mode.lower() == 't':
        DEBUG = True
    elif mode.lower() == 'g':
        DEBUG = False
    else:
        DEBUG = False
        print "Neither g nor t entered. Running in game mode."
    playGame(words)
        
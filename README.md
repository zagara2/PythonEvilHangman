# "Evil"/"Snarky" Hangman!

## What is it?

**Hangman - but the deck is seriously stacked against the player!** 

This was an assignment I completed while studying computer science at Duke University. Instructions for the assignment were as follows:

"Hangman is a traditional children's game, typically played with words. For this assignment you'll program the computer so that it plays a snarky version of the game, some might say diabolically snarky version. Some might say it's a cheating or evil version of hangman. A form of the game dubbed cheating is described on this website. For this program you'll leverage the power of dictionaries and a **greedy algorithm** to program the computer to play a game in which the computer changes its mind, by changing its secret word so that the new secret word is consistent with previous guesses, but harder (perhaps)to guess. The program cheats by making it as difficult as possible to win by categorizing all the possible words based on the letter guessed, and then continuing with the largest category of words and choosing a new secret word from that category.

From the Computer's Viewpoint -

The output below has print-debugging enabled that shows how the computer is "playing" a game of clever-hangman. The secret word is shown before each guess the human player makes. The number of words that could be the secret word is also shown. The human player doesn't know the secret word, she's trying to guess it.

When the game starts, the computer pick a word at random as the secret word, in this case the word curries has been chosen. The player has no misses and no letters of the secret word are shown. Since print-debugging is on, the computer displays the secret word and the number of possibilities for the secret word -- in this case all 7,359 seven-letter words in the computer's lexicon are possible. In the output below the italicized lines (secret word and # of words possible) would normally not be printed as part of the game.

![Example Pic 1][instructions1.JPG]
![Example Pic 1][instructions2.JPG]

Although the user guesses 'i', which is in the computer's secret word, the computer switches secret words so that 'i' is not in the word, and the user has one miss.
As the game progresses the user is shown guessing a letter in the secret word, but for the first time on the third guess --- the secret word waffles is the letter revealed as part of the word.

As the game progresses the user eventually gets eight misses and loses." 

## Technologies Used
* Python

## Grade Recieved
100%
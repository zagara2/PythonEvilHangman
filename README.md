# "Evil"/"Snarky" Hangman!

## What is it?

**Hangman - but the deck is seriously stacked against the player!** 

This was an assignment I completed while studying computer science at Duke University. Instructions for the assignment were as follows:

"Hangman is a traditional children's game, typically played with words. For this assignment you'll program the computer so that it plays a snarky version of the game, some might say diabolically snarky version. Some might say it's a cheating or evil version of hangman. A form of the game dubbed cheating is described on this website. For this program you'll leverage the power of dictionaries and a **greedy algorithm** to program the computer to play a game in which the computer changes its mind, by changing its secret word so that the new secret word is consistent with previous guesses, but harder (perhaps) to guess.

From the Computer's Viewpoint -

The output below has print-debugging enabled that shows how the computer is "playing" a game of clever-hangman. The secret word is shown before each guess the human player makes. The number of words that could be the secret word is also shown. The human player doesn't know the secret word, she's trying to guess it.

When the game starts, the computer pick a word at random as the secret word, in this case the word curries has been chosen. The player has no misses and no letters of the secret word are shown. Since print-debugging is on, the computer displays the secret word and the number of possibilities for the secret word -- in this case all 7,359 seven-letter words in the computer's lexicon are possible. In the output below the italicized lines would normally not be printed as part of the game

Welcome to (Snarky) Hangman:

`(secret word: curries ) # words possible:  7359
Progress:  _ _ _ _ _ _ _
letters missed: 
guess a letter:  i
i  not in secret word`


(secret word: tresses ) # words possible:  4048
Progress:  _ _ _ _ _ _ _
letters missed:  i
guess a letter:  e
you guessed a letter correctly!

(secret word: waffles ) # words possible:  969
Progress:  _ _ _ _ _ e _
letters missed:  i
guess a letter:  a
a  not in secret word

(secret word: toppled ) # words possible:  455
Progress:  _ _ _ _ _ e _
letters missed:  i a
guess a letter:  o
o  not in secret word

(secret word: jumbled ) # words possible:  159
Progress:  _ _ _ _ _ e _
letters missed:  i a o
guess a letter:  u
you guessed a letter correctly!

(secret word: rumbled ) # words possible:  76
Progress:  _ u _ _ _ e _
letters missed:  i a o
guess a letter:  r
r  not in secret word

(secret word: tumbled ) # words possible:  46
Progress:  _ u _ _ _ e _
letters missed:  i a r o
guess a letter:  t
t  not in secret word

(secret word: bundles ) # words possible:  41
Progress:  _ u _ _ _ e _
letters missed:  i a r t o
guess a letter:  s
s  not in secret word

(secret word: buckled ) # words possible:  20
Progress:  _ u _ _ _ e _
letters missed:  a i o s r t
guess a letter:  d
you guessed a letter correctly!

(secret word: lunched ) # words possible:  15
Progress:  _ u _ _ _ e d
letters missed:  a i o s r t
guess a letter:  n
n  not in secret word

(secret word: bumbled ) # words possible:  9
Progress:  _ u _ _ _ e d
letters missed:  a i o n s r t
guess a letter:  m
you guessed a letter correctly!

(secret word: jumbled ) # words possible:  4
Progress:  _ u m _ _ e d
letters missed:  a i o n s r t
guess a letter:  b
you guessed a letter correctly!

(secret word: humbled ) # words possible:  3
Progress:  _ u m b _ e d
letters missed:  a i o n s r t
guess a letter:  l
you guessed a letter correctly!

(secret word: fumbled ) # words possible:  3
Progress:  _ u m b l e d
letters missed:  a i o n s r t
guess a letter:  f
f  not in secret word

You are hung! word was  jumbled

Although the user guesses 'i', which is in the computer's secret word, the computer switches secret words so that 'i' is not in the word, and the user has one miss.
As the game progresses the user is shown guessing a letter in the secret word, but for the first time on the third guess --- the secret word waffles is the letter revealed as part of the word.

As the game progresses the user eventually gets eight misses and loses." 

## Technologies Used
* Python

## Grade Recieved
100%
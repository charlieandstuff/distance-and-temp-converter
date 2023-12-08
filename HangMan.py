wordlist = ["console", "texture", "horse"]
import random
incorrectGuesses = 0
##correctGuesses = 0
Hangword = (random.choice(wordlist))
##creates a list of that can be used to find the length of the word and replace it with an underscroe
hiddenword = list("_" * len(Hangword))
wincondition = 1 * len(hiddenword)
print (" the wordlength is ")
## make it so if you have more than 6 incorrect guesses you die
while incorrectGuesses < 6:
    ##for each character in the 
    for char in hiddenword:
        print (char, end = "")

    Guess = input (" Guess! ")

    # If guess correct
    if Guess in Hangword:
        # Hangword remove Guess
        print ("correct!")
        print (Guess)
        ##correctGuesses += 1
        for i,char in enumerate(Hangword):
             if Guess == char:
                hiddenword [i] = Guess    
    ##else if guess incorrect adds on to inccorect guesses then 
    else:
        print ("Wrong loser")
        incorrectGuesses += 1
        print (f"{incorrectGuesses}" + " out of 6 incorrect guesses")
    ## checks if the word has been completly guessed if so you have escaped and won
    if hiddenword == list(Hangword):
        print ("you won the word was " + Hangword)
        print ("you lost bozo get hung")
        print  ("  ______")
        print  (" l       Snap! ")
        print  (" l           ")
        print  (" l   --   -     -    o ")
        print  (" l    -   --  -     /|\ ")
        print ("/l\\  --  --       - / >_ ")
        break
## you lost
else:
    print ("you lost bozo get hung")
    print  ("  ______")
    print  (" l      ! ")
    print  (" l      0")
    print  (" l     /|\ ")
    print  (" l     / \\")
    print ("/l\\")
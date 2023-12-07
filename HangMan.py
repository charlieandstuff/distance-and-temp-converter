wordlist = ["console", "texture", "horse"]
import random
incorrectGuesses = 0
correctGuesses = 0
Hangword = (random.choice(wordlist))
##creates a list of that can be used to find the length of the word and replace it with an underscroe
hiddenword = list("_" * len(Hangword))
wincondition = 1 * len(hiddenword)
print (" the wordlength is ")

while incorrectGuesses < 6:

    for char in hiddenword:
        print (char, end = "")

    Guess = input (" Guess! ")

    # If guess correct
    if Guess in Hangword:
        # Hangword remove Guess
        print ("correct!")
        print (Guess)
        correctGuesses += 1
        for i,char in enumerate(Hangword):
             if Guess == char:
                hiddenword [i] = Guess

    elif correctGuesses == wincondition:
        print ("you won the word was" + hiddenword)
        break
    
    
    # else if guess incorrect adds on to inccorect guesses then 
    else:
        print ("Wrong loser")
        incorrectGuesses += 1
        print (f"{incorrectGuesses}" + " out of 6 incorrect guesses")

else:
    print ("you lost bozo get hung")
    print  ("  ______")
    print  (" l      ! ")
    print  (" l      o")
    print  (" l    /-+-\ ")
    print  (" l     / \\")
    print ("/l\\")
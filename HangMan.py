wordlist = ["console", "texture", "horse"]
import random
incorrectGuesses = 0
Hangword = (random.choice(wordlist))
##creates a list of that can be used to find the length of the word and replace it with an underscroe
hiddenword = list("_" * len(Hangword))
print (" the wordlength is ")
while incorrectGuesses < 6:

    for char in hiddenword:
        print (char, end = "")

    Guess = input ("Guess! ")

    # If guess correct
    if Guess in Hangword:
        # Hangword remove Guess
        print ("correct!")
        print (Guess) 
        pos = Hangword.index(Guess)
        print(pos)
        # won't get all letters, need to use a loop
        hiddenword[pos]= Guess
    

    # else if guess incorrect
    else:
        print ("Wrong loser")
        incorrectGuesses += 1

else:
    print ("you lost bozo get hung")
    print  ("  ______")
    print  (" l      ! ")
    print  (" l      o")
    print  (" l    /-+-\ ")
    print  (" l     / \\")
    print ("/l\\")
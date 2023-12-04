wordlist = ["console", "texture", "horse"]
import random
Hangword = (random.choice(wordlist))
print (" the wordlength is ")
for char in Hangword:
    print ("_ ", end = "")

Guess = input ("Guess! ")
if Guess in Hangword:
    print ("correct!")
    print

else:
    print ("Wrong you got hung")






## ______
## l    !
## l    O
## l   -i-
## l   / \   
##/l\
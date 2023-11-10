import os
import time

bottles_of_beer = 100

while bottles_of_beer > 0:
    if bottles_of_beer > 1:
        print (f"{bottles_of_beer} bottles of beer on the wall {bottles_of_beer} bottles of beer take one down pass it around ")
        bottles_of_beer = bottles_of_beer - 1
        print (f"{bottles_of_beer} bottles of beer on the wall!")
        print ("I_" * bottles_of_beer)
    
    if bottles_of_beer == 1:
       print (f"{bottles_of_beer} bottle of beer on the wall {bottles_of_beer} bottle of beer take one down pass it around ")
       bottles_of_beer = bottles_of_beer - 1
       print (f"{bottles_of_beer} bottles of beer on the wall!")
       print ("I_" * bottles_of_beer)

    if bottles_of_beer == 0:
        print (f"{bottles_of_beer} bottles of beer on the wall {bottles_of_beer} bottles of beer go to the store buy some more ")
        bottles_of_beer = bottles_of_beer + 100
        print (f"{bottles_of_beer} bottles of beer!")
        break

    time.sleep(1)
    os.system('cls')
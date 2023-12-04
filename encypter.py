
scramble = input ("enter string to encrypt ")
for char in scramble:
  ASCII = ord(char)
  
  ## if statements which determine whether to add or take off 13 to shift the letters into a cyper
  if ASCII > 109 and ASCII < 123 :
      ASCII = ASCII - 13
   
  elif ASCII < 109 and ASCII > 96 :
     ASCII = ASCII + 13
     
  elif ASCII < 78 and ASCII < 96:
     ASCII = ASCII + 13
     
  elif ASCII > 78 and ASCII < 91 :
     ASCII = ASCII - 13
  
  else:
     ASCII = ASCII

  ASCIIconvert = chr(ASCII)
  print(ASCIIconvert, end = "")

#if menuchoice == "encypt":



## assign number to the char using letters dictionary
##add 13 to the number if number goes over 26 start from 13
## assign the number to letters using the numbers dictionary 
## print the output  



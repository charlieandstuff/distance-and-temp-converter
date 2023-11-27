
scramble = input ("enter string to encrypt ")
for char in scramble:
  ASCII = ord(char)
  
  ## 
  if ASCII > 109:
      ASCII = ASCII - 13
  ## 
  elif ASCII < 109:
     ASCII = ASCII + 13
  ASCIIconvert = chr(ASCII)
  print(ASCIIconvert)
 
#if menuchoice == "encypt":



## assign number to the char using letters dictionary
##add 13 to the number if number goes over 26 start from 13
## assign the number to letters using the numbers dictionary 
## print the output  



print ( "welcome to the temperature and distance converter enter 1 to convert temperatures and 2 for distance" )
menuchoice = input ("enter choice: ")

if menuchoice == "1":
    print ( "temperature selected enter unit of temperature C for Celcius, F for Fahrenheit and K for Kevlin " )
    temp_unit = input ("enter selection")
    print (temp_unit + "selected")
    temp_value = input ("enter value of" + temp_unit)
    print (temp_unit + temp_value + "has been chosen what would you like t convert this to?")
    temp_convert_to = input ("what unit")

elif menuchoice == "2":
    print ( "distance selected enter unit of distance" )
    distance_unit = input ("enter")

else:
    endcode 
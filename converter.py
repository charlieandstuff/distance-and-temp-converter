print ( "welcome to the temperature and distance converter enter 1 to convert temperatures and 2 for distance " )
menuchoice = input ("enter choice: ")

if menuchoice == "1":
    print ( "temperature selected enter unit of temperature C for Celcius, F for Fahrenheit" )
    temp_unit = input ("enter selection ")
    print (temp_unit + " selected ")
    temp_value = float (input ("enter value of " + temp_unit + " "))
    print (f"{temp_value}{temp_unit}")

    if temp_unit == "C":
        output = float ((temp_value * 1.8) + 32)
        print (f"{output} + "F")

#else menuchoice == "2":
    #print ( "distance selected enter unit of distance " )
   # distance_unit = input ("enter ")

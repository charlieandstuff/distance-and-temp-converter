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
        print (f"{output}" + "F has been converted from" + f"{temp_value}{temp_unit}")

    elif temp_unit == "F":
        output = float ((temp_value / 1.8) - 32)
        print (f"{output}" + "C has been converted from " + f"{temp_value}{temp_unit}")
        
    else:
        print ("you cant follow simple steps idiot ")
        
elif menuchoice == "2":
    thisdict = {
        "mm": 1,
        "millimeter": 1,
        "cm": 10,
        "centimeter": 10,
        "inch": 25.4,
        "ft":304.8,
        "foot":304.8,
        "m": 1000,
        "meter": 1000,
        "km":1000000,
        "kilometer":1000000,
        "mile":1609344
        }

    print ( "distance selected please enter what measurement you want to use  mm, cm, inch, ft, , m, km or miles " )
    distance_unit = input ("enter ")
    if distance_unit in thisdict:
        convert_from = thisdict[distance_unit]
        print (distance_unit + " selected ")
        distance_value = float (input ("enter value of " + distance_unit + " "))
        
        if distance_unit.isdigit: 
            print (f"{distance_value}{distance_unit}")
            print (" please put in a unit you would like to convert to from your selected " + f"{distance_value}{distance_unit}")
            convert_to = input ("enter unit ")
            convert_unit = thisdict[convert_to]
            if convert_to in thisdict:
               print ("you would like to convert " + f"{distance_value}{distance_unit} " + "into " + f"{convert_to}")
               output_distance = float((distance_value * convert_from) / convert_unit)
               print (f"{output_distance}" + f"{convert_to}")

            else:
                print ("you cant follow simple steps idiot ")
        else:
            print ("you cant follow simple steps idiot ")
    else:
        print ("you cant follow simple steps idiot ")
else:
        print ("you cant follow simple steps idiot ")
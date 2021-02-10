#!/bin/python3

percent = int(input('Enter A percent = '))/100 #A Percentage Value Input 

def percent_(product): #Simple Function to Calculate Our Math 
    total = product - (product * percent)
    print(items,':',total,'LE')
    return()

solid = { #Solid List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 251, "1.5mm": 362,"2mm":480, "3mm": 692, "4mm": 894, "6mm": 1363,"10mm":2201,"16mm":3471
    }
flexible = { #Flixeble List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 286,"1.5mm":412, "2mm": 548, "3mm": 789, "4mm": 1019, "6mm": 1554, "10mm": 2508, "16mm": 3956
    }

for items in solid: 
    print("Solid ") 
    (percent_(solid[items]))

for items in flexible:
    print("Flexible ")
    (percent_(flexible[items])) #BY_Hithmast

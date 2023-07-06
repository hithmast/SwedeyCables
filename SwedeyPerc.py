#!/bin/python3

percent = int(input('Enter A percent = '))/100 #A Percentage Value Input 

def percent_(product): #Simple Function to Calculate Our Math 
    total = product - (product * percent)
    print(items,':',total,'LE')
    return()

solid = { #Solid List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 483.36, "1.5mm": 696.14,"2mm":922.56, "3mm": 1333.12 , "4mm": 1724.93, "6mm": 2584.11,"10mm":4226.73,"16mm":6738.47
    }
flexible = { #Flixeble List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 558.1,"1.5mm":789.72, "2mm": 1043.62, "3mm": 1492.47, "4mm": 1957.16, "6mm": 2877.42, "10mm": 5070.98, "16mm": 7966.84
    }

for items in solid: 
    print("Solid ") 
    (percent_(solid[items]))

for items in flexible:
    print("Flexible ")
    (percent_(flexible[items])) #BY_Hithmast

#!/bin/python3

percent = int(input('Enter A percent = '))/100 #A Percentage Value Input 

def percent_(product): #Simple Function to Calculate Our Math 
    total = product - (product * percent)
    print(items,':',total,'LE')
    return()

solid = { #Solid List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 250.80, "1.5mm": 361.38,"2mm":479.94, "3mm": 691.98, "4mm": 893.76, "6mm": 1362.30,"10mm":2200.20,"16mm":3470.16
    }
flexible = { #Flixeble List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 285.91,"1.5mm":412, "2mm": 547.14, "3mm": 788.88, "4mm": 1018.93, "6mm": 1553.02, "10mm": 2508, "16mm": 3955.80
    }

for items in solid: 
    print("Solid ") 
    (percent_(solid[items]))

for items in flexible:
    print("Flexible ")
    (percent_(flexible[items])) #BY_Hithmast

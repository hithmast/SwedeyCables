#!/bin/python3

percent = int(input('Enter A percent = '))/100 #A Percentage Value Input 

def percent_(product): #Simple Function to Calculate Our Math 
    total = product - (product * percent)
    print(items,':',total,'LE')
    return()

solid = { #Solid List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 253, "1.5mm": 365,"2mm":482, "3mm": 695, "4mm": 895, "6mm": 1365,"10mm":2210,"16mm":3471
    }
flexible = { #Flixeble List for Swedey CopperWire Coated With PVC Max 75 C
    "1mm": 287,"1.5mm":413, "2mm": 549, "3mm": 790, "4mm": 1020, "6mm": 1555, "10mm": 2510, "16mm": 3957
    }

for items in solid: 
    print("Solid ") 
    (percent_(solid[items]))

for items in flexible:
    print("Flexible ")
    (percent_(flexible[items])) #BY_Hithmast

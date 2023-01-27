"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


def dose_amount():
    print("Day One Dosing Guidelines")
    print("")
    print("CHOOSE DIAGNOSIS")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    print("5 - Quit()")
    diagnosis = int(input("Enter a number: "))
    return diagnosis
    
def BMI_input():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb or 21.0 kg")
    weight_input = input("Enter weight: ")
    return weight_input

def weight_conversion():
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
#weight factor can be used as an entry
    return weight 

def dosage_calculation(diagnosis,weight):   
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    print("CORRECT DOSAGE")
    print("For a patient weighing {} kg,".format(round(weight))
    print("  the correct dosage is {} mg the first day"
          .formatround(dosage_mg_first_day))

diagnosis=dose_amount()
weight_input = BMI_input()
weight=weight_conversion()
dosage_calculation(diagnosis,weight)

if __name__ == '__main__':
    dose_amount()
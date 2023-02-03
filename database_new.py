def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient=[patient_name, patient_mrn, patient_age,[]]
    return new_patient

def main_driver():
    db=[]
    db.append(create_patient_entry("Arun John",1,28))
    db.append(create_patient_entry("Jiby Krishna",2,28))
    add_test_to_patient(db,1,"HDL",120)
    add_test_to_patient(db,2,"LDL",100)
    add_test_to_patient(db,2,"HDL",90)
    print(db)
    room_numbers=["102","232","111"]

    print(db)
    print_directory(db,room_numbers)

    #print(db[1] [2])
    #print("Get patient Arun")
#     mrn_to_find=4
#     found_patient=get_patient_entry(db,mrn_to_find)
#   #  if found_patient is False:
#     if found_patient == False:
#         print("Patient mrn {} is not found".format(mrn_to_find))
#     else:
#         print(found_patient)

def print_directory(db,room_numbers):
    for i,patient in enumerate(db):
        print("patient {} is in room {}".format(patient[0],room_numbers[i]))

def get_patient_entry(db,mrn_to_find):
    for patient in db:
        if patient[1]==mrn_to_find:
            return patient
    return False 

def add_test_to_patient(db,mrn_to_find,test_name,test_value):
    patient=get_patient_entry(db,mrn_to_find)
    if patient == False:
        print("Bad Entry")
    else:
        patient[3].append([test_name,test_value])
    return

if __name__ == "__main__":
    main_driver()

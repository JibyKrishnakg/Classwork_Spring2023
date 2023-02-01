def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient=[patient_name, patient_mrn, patient_age]
    return new_patient

def main_driver():
    db=[]
    db.append(create_patient_entry("Arun John",1,28))
    db.append(create_patient_entry("Jiby Krishna",2,28))
    print(db)
    #print(db[1] [2])
    print("Get patient Arun")
    mrn_to_find=4
    found_patient=get_patient_entry(db,mrn_to_find)
  #  if found_patient is False:
    if found_patient == False:
        print("Patient mrn {} is not found".format(mrn_to_find))
    else:
        print(found_patient)

def get_patient_entry(db,mrn_to_find):
    for patient in db:
        if patient[1]==mrn_to_find:
            return patient
    return False 

if __name__ == "__main__":
    main_driver()
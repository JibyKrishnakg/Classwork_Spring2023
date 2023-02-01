def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient=[patient_name, patient_mrn, patient_age]
    return new_patient

def main_driver():
    db=[]
    db.append(create_patient_entry("Arun John",1,28))
    db.append(create_patient_entry("Jiby Krishna",2,28))
    print(db)

if __name__ == "__main__":
    main_driver()
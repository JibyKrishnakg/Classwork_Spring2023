def interface(): 
    print("Blood calculator") 
    while True:
        print("Option:") 
        print("9-Quit") 
        choice = input("Select an option:") 
        if choice=="9": 
            return
interface()

def interface(): 
    print("Blood calculator") 
    k=True
    while k:
        print("Option:") 
        print("9-Quit") 
        choice = input("Select an option:") 
        if choice=="9": 
            k=False
    print("Program ending")
interface()
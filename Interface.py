print("This is the interface.py file")
print("Python thinks this is called {}".format(__name__))

# interface [command marker]


def interface():
    print("Blood calculator")
    k = True
    while k:
        print("Option:")
        print("1: HDL")
        print("2: LDL")
        print("3: Total Cholesterol")
        print("9: Quit")
        choice = input("Select an option:")
        if choice == "9": 
            k=False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice=="3":
            TOTAL_driver()  
    print("Program ending")

#HDL driver
def HDL_driver():
    input1=generic_input()
    result1=HDL_analysis(input1)
    generic_output(input1,result1)

#HDL Classifier
def HDL_analysis(HDL_int): 
    if HDL_int>=60: 
        ans1="Normal" 
    elif 40<=HDL_int<60: 
        ans1="Border line" 
    else: 
        ans1="Low" 
    return ans1 

#LDL driver
def LDL_driver():
    input2=generic_input()
    result2=LDL_analysis(input2)
    generic_output(input2,result2)

#LDL Classifier
def LDL_analysis(LDL_int): 
    if LDL_int<130: 
        ans2="Normal" 
    elif 130<= LDL_int<159: 
        ans2="Border line" 
    elif 160<=LDL_int<189: 
        ans2="High" 
    else: 
        ans2="Very high" 
    return ans2 

def TOTAL_driver():
    input3=generic_input()
    result3=TOTAL_analysis(input3)
    generic_output(input3,result3)

#TC Classifier
def TOTAL_analysis(Total_int): 
    if Total_int<200: 
        ans3="Normal" 
    elif 200<=Total_int<239: 
        ans3="Border line" 
    elif Total_int>=240: 
        ans3="High" 
    return ans3 

#Generic input
def generic_input(): 
    input_bp=input("Enter the Parameter Value:") 
    input_bp=int(input_bp) 
    return input_bp 

#Generic Output
def generic_output(input,result):
    print("The value is {} : {}".format(input,result))

if __name__ == "__main__":
    interface()
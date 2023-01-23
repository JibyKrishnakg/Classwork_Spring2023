def interface(): 

    print("Blood calculator") 
    keep_running= True 
    while keep_running: 
        print("Option:") 
        print("9-Quit") 
        choice = input("Select an option:") 
        if choice=="9": 
            keep_running=False 
        elif choice =="1": 
            HDL_driver() 
    print("Program ending") 

 
 
def HDL_driver(): 
    HDL_in=HDL_input() 
    HDL_analy=HDL_analysis(HDL_in) 

    

def HDL_input(): 
    HDL=input("Enter the result:") 
    HDL=int(HDL_value) 
    return HDL 

 adaldkakd
 

def HDL_analysis(HDL_int): 
    if HDL_int>=60: 
        ans="Normal" 
    elif 40<=HDL_int<60: 
        ans="Border line" 
    else: 
        ans="Low" 
    return ans 

interface() 
HDL_driver()
HDL_analysis(HDL_int)


------------------------------ 

def interface(): 
    print("Blood calculator") 
    keep_running= True 
    while keep_running: 
        print("Option:") 
        print("9-Quit") 

choice = input("Select an option:") 

if choice=="9": 

keep_running=False 

elif choice =="1": 

HDL_driver() 

print("Program ending") 

 
 

def HDL_driver(): 

HDL_in=HDL_input() 

HDL_analy=HDL_analysis(HDL_in) 

 
 

def HDL_input(): 

HDL=input("Enter the result:") 

HDL=int(HDL_value) 

return HDL 

 
 

def HDL_analysis(HDL_int): 

if HDL_int>=60: 

ans="Normal" 

elif 40<=HDL_int<60: 

ans="Border line" 

else: 

ans="Low" 

return ans 

def HDL_output(HDL_value,HDL_analy): 

print("The HDL result of {} is considered to {}".format(),.format()) 

interface() 

 


print("This is the database.py file")
print("Python thinks this is called {}".format(__name__))

import Interface as bc
HDL=55
HDL_analysis=bc.HDL_analysis(HDL)
print("HDL value is {}".format(HDL_analysis)) 
LDL_int=bc.generic_input()
print (bc.LDL_analysis(LDL_int))

# from Interface import HDL_analysis, generic_input
# HDL=90
# HDL_analysis=HDL_analysis(HDL)
# print("HDL value is {}".format(HDL_analysis)) 
# generic_input()

# from interface import * : Not recommended


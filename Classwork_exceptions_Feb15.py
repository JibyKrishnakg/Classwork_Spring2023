my_data = [1,2]
a = my_data[7]
print(a)

try:
    my_data = [1,2]
    a = my_data[7]
    print(a)
except IndexError:
    print("Index error is found")
    
"""
def my_function():
    my_data = [1,2]
    a = my_data[7]
    print(a)
    return a

if __name__ == "main":
    b = my_function()
    print(b)

def my_function():
    try:
        from 
    my_data = [1,2]
    a = my_data[7]
    print(a)
    return a

if __name__ == "main":
    b = my_function()
    print(b)
"""
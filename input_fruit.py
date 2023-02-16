"""
in_file = open("input_data","r")
fruits = in_file.readlines()
print(fruits)
in_file.close()
"""
def read_file():
    in_file = open("input_file.txt","r")
    first_line = in_file.readlines()
    patient_data =first_line.strip("\n").split
    patient_id = int(patient_data[1])
    return patient_id

def test_read_file():
    from module import read_file
    filename = "my_test_data.txt"
    answer = read_file(filename)
    expected = 50
    assert == expected
    
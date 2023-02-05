# def test_check_fever():
#     from interface import test_check_fever
#     input_temps = [97,98,100,103,91]
#     answer = check_fever(input_temps)
#     expected = True
#     assert answer == expected

input_list = [97,98,91,110,104]
def test_check_fever():
    answer=check_fever(input_list)
    expected = True
    assert answer == expected
    print("The patient is suffering from fever.")

def check_fever(input_list):
    for temperature in input_list:
        if temperature>100.5:
            return True
    return False


test_check_fever()
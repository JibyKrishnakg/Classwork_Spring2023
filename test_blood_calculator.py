def test_HDL_analaysis():
    from Interface import HDL_analysis
    # Arrange
    HDL_input=65
    # Act
    answer=HDL_analysis(HDL_input)
    # Assert
    assert answer == "Normal"

def test_HDL_analaysis_borderline():
    from Interface import HDL_analysis
    # Arrange
    HDL_input=45
    # Act
    answer=HDL_analysis(HDL_input)
    # Assert
    assert answer == "Border line"

def test_HDL_analaysis_low():
    from Interface import HDL_analysis
    # Arrange
    HDL_input=30
    # Act
    answer=HDL_analysis(HDL_input)
    # Assert
    assert answer == "Low"

# pytest: One function Decorator
# Decorator functions gives additional functionality
# Variables separated by comma, List of values to the variables assigned
# Pathway check : each branch/pathway for range of inputs must be checked
# Check all reasonable numbers
# User intervention Yes [not pytest applicable]
# Companies specific Style guide for easy readability "Variable name", "checker points" 
# Python has PEP 8 Style guide
# Order in the pytest decorator need not match with the function input parameters
# List of items under pytest decorator can be taken as separate variable and add variable name to the decorator


import pytest

@pytest.mark.parametrize("HDL_input,expected", 
[(65, "Normal"),(45, "Border line"),(20,"Low"),(5,"Low"),(61,"Normal")])
def test_HDL_analaysis(HDL_input,expected):
    from Interface import HDL_analysis
    # Arrange
    # Act
    answer=HDL_analysis(HDL_input)
    # Assert
    assert answer==expected

import pytest

@pytest.mark.parametrize("LDL_input,expected", 
[(120, "Normal"),(135, "Border line"),(165,"High"),(190,"Very high")])
def test_LDL_analaysis(LDL_input,expected):
    from Interface import LDL_analysis
    # Arrange
    # Act
    answer=LDL_analysis(LDL_input)
    # Assert
    assert answer==expected

# Not a best practice
# Testing stops in the line and cannot know others are right or not
# No multiple asserts on the same function

# def test_HDL_analaysis():
#     from Interface import HDL_analysis
#     # Arrange
#     HDL_input=65
#     # Act
#     answer=HDL_analysis(HDL_input)
#     # Assert
#     assert answer=="Normal"
#     HDL_input=65
#     # Act
#     answer=HDL_analysis(HDL_input)
#     # Assert
#     assert answer=="Normal"
#     HDL_input=65
#     # Act
#     answer=HDL_analysis(HDL_input)
#     # Assert
#     assert answer=="Normal"
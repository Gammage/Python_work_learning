from eleven_three_employee import Employee
import pytest

@pytest.fixture
def test_employee_raise():
    """test the employee raise amounts"""
    return Employee('ben','gammage',80000)

def test_give_default_raise(test_employee_raise):
    """test the default raise amount"""
    test_employee_raise.give_raise()
    assert test_employee_raise.annual_salary == 85000
    
def test_give_custom_raise(test_employee_raise):
    """test the custom raise amount"""
    test_employee_raise.give_raise(3000)
    assert test_employee_raise.annual_salary == 83000
    
@pytest.fixture
def john():
    """he will do this job adding 1+2"""
    c = 1 + 2
    return c

def test_add(john):
    """test the default raise amount"""
    assert john == 3
    
##example of different use of naming conventions
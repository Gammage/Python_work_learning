from name_function import get_formatted_name

def test_first_last_name():
    """do names like 'janis joplin' work?"""
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'
    
def test_first_last_middle_name():
    """do names like 'benjamin james gammage' work?"""
    formatted_name = get_formatted_name('benjamin','gammage','james')
    assert formatted_name == 'Benjamin James Gammage'
    
#naming is important, it must start with test_
#when asking pytest to run the tests we've written, it will look for any file
#that begins with test_
    #runs all of the tests it finds in file
    
#in the test file, we first import the function we want to test
#then we define the test a function, test_first_last_name
    #longer name:
        #test functions start with word test_ will be discovered by pytest
        #should be more longer and descriptive - never be called yourself, tests
        #will be run by pytest
#an assertion is a claim about a condition. here we're claiming that the value of
#formatted_name should be 'janis joplin'


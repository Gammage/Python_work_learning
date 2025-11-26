def get_formatted_name(first,last,middle=""):
    """generate a neatly formatted name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

#responding to a failed test
#assuming right conditions are checked,
    #when a test fails you dont change the test
#
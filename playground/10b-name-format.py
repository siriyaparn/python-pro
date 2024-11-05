def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"{formated_f_name} {formated_l_name}")
    print("This will be not printed.") # This line will not be printed, return tell the computer that this is the end of function

# Input 
f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
format_name(f_name, l_name)
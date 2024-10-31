def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return(f"{formated_f_name} {formated_l_name}")

# Input 
f_name = input("First name: ")
l_name = input("Last name: ")
format_name(f_name, l_name)
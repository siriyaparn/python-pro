num_char = len(input("What is your name?"))
## If you print above code, you will get TypeError
# print("Your name has " + num_char + " characters.")

# str: convert int to str
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Type conversion
# type command is used to investigate data type
## int: convert data to int
a = "123"
print(type(a))
# output: str

a = int(a)
print(type(a))
# output: int

## float: convert data to float
a = float(a)
print(type(a))
# output: float

print(70 + float("100.5"))
# output: 170.5 

## str: convert data to str
print(str(70) + str(100))
# output: 70100 
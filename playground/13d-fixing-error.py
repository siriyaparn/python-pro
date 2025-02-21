try:
    age = int(input("How old are you? :"))
except ValueError:
    print("You are typed in a an invalid number. Please try again with a numerical response such as 15.")

if age > 18:
    print(f"You can drive at age {age}")
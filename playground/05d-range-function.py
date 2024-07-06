# For loop with range
for number in range (1,11):
    print(number)
    ## output: 1 2 3 4 5 6 7 8 9 10

for number in range (1,11,3):
    print(number)
    ## output: 1 4 7 10

# Create Gauss's value
total = 0
for number in range(1,101):
    total += number
print(total)
## output = 5050
# Create list of U.S. states
# Use list to store many pieces of related data with the order
states_of_america = ["Delaware", "Pencilvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", 
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Winconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Note: list has a offset or shift of 0. (start index at 0)
print(states_of_america[0])
## output: Delaware

# Get last item in the list
print(states_of_america[-1])
## output: Hawaii

print(states_of_america[-2])
## output: Alaska

# Edit data in the list
states_of_america[1] = "Pennsylvania"
print(states_of_america)
## output: "Pencilvania" is changed to "Pennsylvania"

# Add an item at the end of the list
states_of_america.append("Alice Land")
print(states_of_america)
## output: ... , 'Alaska', 'Hawaii', 'Alice Land'

# Add an additional list
states_of_america.extend(["Belle Land", "Cindy Land"])
print(states_of_america)
# output: ... , 'Alaska', 'Hawaii', 'Alice Land', 'Belle Land', 'Cindy Land'

# Find total items
num_of_state = len(states_of_america)
print(states_of_america[num_of_state - 1])
from prettytable import PrettyTable

# Create object
table = PrettyTable()

# Set field names
table.field_names = ["Pokemon Name", "Type"]

# Add rows
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Squirtle", "Fire"],
    ]
)

# Add columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Squirtle"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change attributes
table.align = "l"

print(table)
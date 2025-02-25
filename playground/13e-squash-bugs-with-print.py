word_per_page = 0

page = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # Here is the bug

total_words = page * word_per_page

print(f"page = {page}")
print(f"word_per_page = {word_per_page}")
print(total_words)

## Test
# Number of pages: 45
# Number of words per page: 250
# page = 45
# word_per_page = 0 -> something to do with this
# 0
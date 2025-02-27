import random
import maths

def mutate(a_list):     # a_list: [1, 2, 3, 5, 8, 13]
    b_list = []         # b_list: [] 
    new_item = 0        # new_item: 0 then 1 and so on.. 
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(a:1, b:3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
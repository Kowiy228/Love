fruits = ["apple", "banana", "orange", "pear", "watermelon", "apple", "banana"]
unique_fruits = list(set(fruits))
print(unique_fruits)

first_three_items = unique_fruits[:3]
last_two_items = unique_fruits[-2:]
print("First 3 items: ", first_three_items)
print("Last 2 items: ", last_two_items)
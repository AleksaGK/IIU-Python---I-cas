# Lista je uređena kolekcija koja je promenljiva i dozvoljava dupliranje elemenata

# Create list
numers = [1, 2, 3, 4, 5]

# use a consturctor
numbers2 = list((1, 2, 3, 4, 5))

# print(numers, numbers2)

fruits = ['Apples', 'Oranges', 'Lemons', "Bananas"]

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove("Lemons")
# Remove with pop
fruits.pop(2)

# Insert into position
fruits.insert(2, 'Grapes')

# Change value
fruits[0] = "Watermelon"

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

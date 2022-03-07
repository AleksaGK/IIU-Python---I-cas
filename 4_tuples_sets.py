# Tuple je uređena kolecija koju nije moguće promeniti. Dozvoljava duple članove

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)
fruits2 = ('Apples',)
"""
fruits2 = ('Apples')  # Apples <class 'str'>
fruits2 = ('Apples',)  # ('Apples',) <class 'tuple'>
print(fruits2, type(fruits2))
"""

# Get value
print(fruits[1])

# Can't change value
fruits[0] = "Pears"

# Delete tuple
del fruits2
print(fruits2)

# Get length
print(len(fruits))


# Set je neuređena kolekcija i bez indeksa. Nema duplih članova

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add('Grape')
fruits_set.add('Grape')
fruits_set.add('Grape')

# Remove from set
fruits_set.remove("Grape")

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)

# Rečnik (Dictionary) je neuređena, promenljiva i indeksirana kolekcija. Ne dozvoljava dupliranje članova

# Create dict
person = {
    'first_name': 'Aleksa',
    'last_name': 'Miletic',
    'age': 24
}

# Use constructor
person2 = dict(first_name='Marko', last_name='Markovic')
print(person2, type(person2))
print(person)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dictionary keys
print(person.keys())

# Get dictionary items
print(person.items())

# Get dictionary values
print(person.values())

# Copy dict
person2 = person.copy()
person2['city'] = "Beograd"

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Pera', 'age': 23},
    {'name': 'Ana', 'age': 21},
]

# print(people)
print(people[1]['name'])

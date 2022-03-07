# Petlja se koristi za iteraciju sekveni (koristi se za list, tuple, dictionary, set ili string).

people = ['Aleksa', 'Marko', 'Ana', 'Marija']

# Simple for loop
for person in people:
    print(f'Current person: {person}')
else:
    print('End')

# Break
for person in people:
    if person == 'Ana':
        break
    print(f'Current person: {person}')

# Continue
for person in people:
    if person == 'Ana':
        continue
    print(f'Current person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

for i in range(0, 11, 2):
    print(f'Number: {i}')

# While petlja izvršava kod dokle god je uslov ispunjen

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
else:
    print("End")

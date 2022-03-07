# If/ Else su uslovi koji se koriste da odluče šta će se dalje izvršavaati, bazirano na true ili false vrednostima

x = 10
y = 5

# Operatori poređenja (==, !=, >, <, >=, <=) - koriste se da porede vrednosti

# If
if x > y:
    print(f'{x} is greater then {y}')

y = 50
# If/else
if x > y:
    print(f'{x} is greater then {y}')
else:
    print(f'{y} is greater then {x}')
y = 10
# elif
if x > y:
    print(f'{x} is greater then {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater then {x}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'x is grater then 2 and less then or equal to 10')


# Logički operatori (and, or, not) - Koriste se da kombinuju uslove
print('----')
# and
if x > 2 and x <= 10:
    print(f'x is grater then 2 and less then or equal to 10')
# or
if x > 2 or x <= 10:
    print(f'x is grater then 2 or less then or equal to 10')

y = 20
# not
if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership Operators (in, not in) - Membership operators se koriste da provere da li je neka sekvenca prisutna u nekom objektu

print('----')
x = 3
numbers = [1, 2, 3, 4, 5]
# in
if x in numbers:
    print(x in numbers)

x = 13
# not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Porede objekte, ne po tome da li su jednaki, već po tome da li su to isti objekti (da li imaju istu adresu)

print('----')
x = 20
# is
if x is y:
    print(x is y)
# is not
x = 13
if x is not y:
    print(x is not y)

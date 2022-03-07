# Stringovi u python-u su okruženi jednostrukim ili dvostrukim navodnicima. Proćićemo formatiranje stringa i neke string metode

name = "Marko"
age = 37

# Concatenate
# možemo da spajamo samo stringove
print('Hello, my name is '+name+" and I am "+age)
print('Hello, my name is '+name+" and I am "+str(age))

# String Formatting

# Arguments by position
print("My name is {name} and I an {age}".format(
    name=name, age=age))  # kao extension method u C#-u

# F-string (3.6+)
print(f"Hello, my name is {name} and i am {age}")

# String Methods
s = "hello world"

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position (first occurence)
print(s.find('r'))

# ova 3 su False zbog razmaka, da nema razmaka prva 2 su True
# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

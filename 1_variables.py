# Varijabla je kontejner za vrednost, koja može biti različitih tipova


'''
Ovo je višelinijski komentar
ili docstring (koristi se za definisanje svrhe funkcije)
mogu biti je jednostruki i dvostruki navodnici
'''

"""
PRAVILA ZA VARIJABLE:
  - Varijable su case sensitive (name i NAME su različite varijable)
  - MOra početi slovom ili donjom crtom (_)
  - Može imati brojeve u sebi, ali ne sme početi brojem
"""

x = 1             # int
y = 2.5           # float
name = "Aleksa"   # string
is_cool = True    # bool

# Multiple assignmetn
x, y, name, is_cool = (1, 2.5, "Aleksa", True)

# Basic math
a = x+y

print(x, y, name, is_cool, a)

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(x))
print(type(y), y)
print(type(z), z)

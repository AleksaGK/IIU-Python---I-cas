# Funkcija je blok koda koja se pokreće samo kada se pozove. U Python-u se ne koriste {}, već se koriste tabulatori i razmaci

# Create function
def sayHello(name="Pera"):
    print(f'Hello {name}')


sayHello('Aleksa Miletic')
sayHello()

# Return value


def getSum(num1, num2):
    total = num1+num2
    return total


num = getSum(1, 5)
print(num)


# Lambda funkcija je mala anonimna funkcija.
# Lambda funkcija može da primi bilo koji broj parametara ali može imati samo jedan izraz. Slična je arrow funkcijama u JS-u


# getSum = lambda num1, num2 : num1 + num2
def getSum(num1, num2): return num1 + num2


print(getSum(10, 3))

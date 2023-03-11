interest = 1.59
term = "36"
creditName = "Need Credit"

print(type(interest))  # float
print(type(term))  # str
print(type(creditName))  # str

# print(term + 12) # TypeError: can only concatenate str (not "int") to str
# print(int(creditName)) # ValueError: invalid literal for int() with base 10: 'Need Credit'

print(int(term) + 12)  # 48

interest = str(interest)
print(type(interest))  # str

term = 36  # int(input("Please enter the term amount: "))
print(type(term))  # str

term = term + 12

# String interpolation
print("The term you selected is: " + str(term))
print("The term you selected is: {termNumber}".format(termNumber=term))
print(f"The term you selected is: {term}")

name = "Joe"
text = "Hello {name}".format(name="John")
print(text)

text = f"Welcome {name}"
print(text)

# Lists
array = ["Need Credit", 10, 5.2, True]
print(array)  # ['Need Credit', 10, 5.2, True]

loans = ["Need Credit", "Vehicle Credit", "Home Credit"]
print(type(loans))  # list

print(loans)  # ['Need Credit', 'Vehicle Credit', 'Home Credit']
print(loans[0])  # Need Credit

# print(loans[3]) # IndexError: list index out of range

print(len(loans))  # 3

loans.append("Special Credit")  # Add element to the end of the list
print(loans)  # ['Need Credit', 'Vehicle Credit', 'Home Credit', 'Special Credit']

loans.append("X Credit")
print(loans)  # ['Need Credit', 'Vehicle Credit', 'Home Credit', 'Special Credit', 'X Credit']

loans.pop(0)
print(loans)  # ['Vehicle Credit', 'Home Credit', 'Special Credit', 'X Credit']

loans.append("Vehicle Credit")
print(loans)  # ['Vehicle Credit', 'Home Credit', 'Special Credit', 'X Credit', 'Vehicle Credit']

loans.remove("Vehicle Credit")
print(loans)  # ['Home Credit', 'Special Credit', 'X Credit']

loans.extend(["Y Credit", "Z Credit"])
print(loans)  # ['Home Credit', 'Special Credit', 'X Credit', 'Y Credit', 'Z Credit']

# Loops
for i in range(10):
    print(i)  # 0 1 2 3 4 5 6 7 8 9

print("===============")

for i in range(5, 10):
    print(i)  # 5 6 7 8 9

print("===============")

for i in range(0, 51, 10):
    print(i)  # 0 10 20 30 40 50

print("===============")

# for i in range(0.1, 0.5):
#     print(i)  # TypeError: 'float' object cannot be interpreted as an integer

loans = ["Need Credit", "Vehicle Credit", "Home Credit"]

for loan in loans:
    print(loan)  # Need Credit Vehicle Credit Home Credit

print("===============")

for i in range(len(loans)):
    print(loans[i])  # Need Credit Vehicle Credit Home Credit

print("===============")

# while True:
#     print("x") # Infinite loop

i = 0
while i < 10:
    print("x")  # x x x x x x x x x x
    i += 1
print("y")

print("===============")

while True:
    print("x")  # x
    break

print("===============")

i = 0
while i < len(loans):
    i += 1
    print(loans[i])
    if loans[i] == "Home Credit":
        break

print("=====Functions=====")

# Functions
price = 100
discount = 20


def calculate():
    print(100 - 20)


def calculateWithParams(price, discount):
    print(price - discount)


def sayHello(name):
    print(f"Hello {name}")


calculate()
calculateWithParams(100, 20)
calculateWithParams(price, discount)
sayHello("John")
sayHello("Joe")


def calculateAndReturn(price, discount):
    return price - discount


newPrice = calculateAndReturn(200, 50)
print(newPrice)  # 150


# void function
def calculatePrice(price, discount):
    print(price - discount)


# return value function
def calculatePriceAndReturn(price, discount):
    return price - discount


print("===============")
func1 = calculatePrice(100, 50)
func2 = calculatePriceAndReturn(300, 100)

print(func1)  # None
print(func2)  # 200

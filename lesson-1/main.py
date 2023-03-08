print("kodlamaio")

# variableName = value(int, float, string, boolean)
title = "Car Loan"  # string => metinsel ifade

print(title)

title = "Need Loan"  # string => metinsel ifade

print(title)

expiration = 36  # int => tam sayı
addExpiration = 6  # int => tam sayı

expiration2 = "36"  # string => metinsel ifade

monthlyPayment = 200.50  # float => ondalıklı sayı

isRise = True  # boolean => true or false

# Math Operators

# + => plus
print(5 + 5)  # 10
print(expiration + 12)  # 48
print(expiration + addExpiration)  # 42
print(36 + 6)  # 42

# - => minus
print(5 - 5)  # 0
print(expiration - 12)  # 24
print(expiration - addExpiration)  # 30
print(36 - 6)  # 30

# * => times
print(5 * 5)  # 25
print(expiration * 12)  # 432
print(expiration * addExpiration)  # 216
print(10 * 10)  # 100

# / => divide
print(5 / 5)  # 1.0
print(expiration / 2)  # 18.0
print(expiration / addExpiration)  # 6.0
print(10 / 2)  # 5.0

newExpiration = expiration / 2
price = 100
discountedPrice = price - 20

print(newExpiration)  # 18.0
print(discountedPrice)  # 80

# % => mod
print(10 % 2)  # 0
print(expiration % 5)  # 1
print(expiration % addExpiration)  # 0
print(30 % 10)  # 0

# Boolean Operators

# == => is equal to
print(1 == 1)  # True
print(1 == 2)  # False

# > => greater than
print(1 > 2)  # False
print(3 > 1)  # True
print(1 > 1)  # False
print(1 >= 1)  # True

# < => less than
print(1 < 2)  # True
print(3 < 1)  # False
print(1 < 1)  # False
print(1 <= 1)  # True

# != => not equal to
print(1 != 1)  # False
print(1 != 2)  # True

# or => or
# one of them should be true to get true result
print(1 > 2 or 5 > 2)  # (false or true) => true
print(1 > 2 or 5 > 2 and 3 > 2)  # (false or true and true) => true
print(1 > 2 and 5 > 2 and 3 > 2)  # (false and true and true) => false
print(2 > 1 or 1 > 2 and 3 > 2)  # (true or false and true) => true

# and => and
# both of them should be true to get true result
print(1 > 2 and 5 > 2)  # (false and true) => false

# If Statement

# if condition:
#     code block

number1 = 15
number2 = 15

if number1 < number2:
    print("number1 is greater than number2")
    print("inside of if block")
elif number1 == number2:
    print("number1 is equal to number2")
    print("inside of elif block")
else:
    print("number2 is greater than number1")
    print("inside of else block")

print("outside of if block")

if number1 <= number2:
    print("number1 is less than or equal to number2")
if number1 == number2:
    print("number1 is equal to number2")
else:
    print("number2 is greater than number1")

# result => number1 is less than or equal to number2, number1 is equal to number2

if number1 < number2:
    print("number1 is less than or equal to number2")
    if number1 == number2:
        print("number1 is equal to number2")
else:
    print("number2 is greater than number1")

# result => number2 is greater than number1

# Basic Syntax & IO
# 1. priting Hello,World!
print("Hello,World!")
# 2. Take user input and print
# name=input("Enter your name:")
# print("Hello,",name,'!')

# 3.swap two numbers
a=10 #assigning 10 to a  
b=5 # assigning 5 to b
a,b=b,a # swapping the values 
print(a,b)

# 4.check if a number is even or odd 
# let us take input x with user to check given number is even or odd
# x=int(input("enter number to check even or odd:"))
# if x%2==0:
#     print(x,"is even number")
# else:
#     print(x, "is odd number")

# 5.find the largest of 2 numbers
x=2
y=10
if x>y:
    print(x,"is greater than",y)
else:
    print(y,"is greater than",x)

# Operators
'''1.perform arthematic operations
(+, -, *, /, %, **), 
take any values as “a” and “b” '''
a=100
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# 2.calculate the sqaure and cube of a number
# z=int(input("Enter a number to find sqaure and cube:"))
# square=z**2
# print(f"The sqare of a {z} is {square}")
# cube=z**3
# print(f"The cube of a {z} is {cube}")

# 3. convert Celsius to Fahrenheit (F = (C * 9/5) + 32).
celsius=28.4
fahrenheit= (celsius*9/5)+32
print(f"{celsius} celsius :{fahrenheit} fahrenheit")

#4. convert kilometers to miles (1 km = 0.621371 miles)
km=10
miles=0.621371
converted_miles=km*miles
print(f"{km} kilometers ={converted_miles} miles")

#5. check if a number is positive,negative,zero
# check=int(input("enter a number to find if positive, negative or zero:"))
# if check==0:
#     print(f"{check} is zero")
# elif check>0:
#     print(f"{check} is Positive")
# else:
#     print(f"{check} is Negative")

# conditional statements
# 1.find the largest of three numbers
a,b,c=20,289,100
if a>=b and a>=c:
    print(f"{a} is Highest amoung three numbers")
elif b>=a and b>=c:
    print(f"{b} is Highest amoung three numbers")
else:
    print(f"{c} is Highest amoung three numbers")

''' 2. check if a year is a leap year. A leap year is a year that is divided by 4,
but if it is a century year (divisible by 100),  
it must also be divisible by 400 to be a leap year.'''

# year=int(input("Enter a number to check if it is a Leap Year:"))

# if (year % 4==0 and year % 100!=0) or (year % 400==0):
#     print(f"{year} is leap year")
# else: 
#     print(f"{year} is not leap year")

# 3. Check if a character is a vowel or consonant

character=input("enter a char:")
vowels= "aeiou"
if character in vowels:
    print(f"{character} is vowel")
elif character.isalpha():
    print(f"{character} is consonant")
else: 
    print(f"{character} is invalid input please enter letters")






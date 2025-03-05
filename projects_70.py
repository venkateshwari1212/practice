# Basic Syntax & IO
# 1. priting Hello,World!
print("Hello,World!")
# 2. Take user input and print
# name=input("Enter your name:")
# print("Hello,",name,'!')

# 3.swap two numbers
# a=10 #assigning 10 to a  
# b=5 # assigning 5 to b
# a,b=b,a # swapping the values 
# print(a,b)

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

# character=input("enter a char:")
# vowels= "aeiou"
# if character in vowels:
#     print(f"{character} is vowel")
# elif character.isalpha():
#     print(f"{character} is consonant")
# else: 
#     print(f"{character} is invalid input please enter letters")

# 4. Write a Python program to assign the grades to each subject based on the grade scale: 
#  Student subject marks:
#  maths = 85
#  science = 78
#  english = 92
#  Grade scale:
#  A: 90-100
#  B: 80-89
#  C: 70-79
#  D: 60-69
#  E: 50-59
#  F: Below 50 

maths=85
science=78
english=92
if maths<=100 and maths>=90:
    maths_grade= "A"
elif maths<=89 and maths>=80:
    maths_grade= "B"
elif maths<=79 and maths>=70:
    maths_grade= "C"
elif maths<=69 and maths>=60:
    maths_grade= "D"
elif maths<=59 and maths>=50:
    maths_grade= "E"
elif maths<=49:
    maths_grade= "F"
else:
    print(f"{maths} invalid marks")

if science<=100 and science>=90:
    science_grade= "A"
elif science<=89 and science>=80:
    science_grade= "B"
elif science<=79 and science>=70:
    science_grade= "C"
elif science<=69 and science>=60:
    science_grade= "D"
elif science<=59 and science>=50:
    science_grade= "E"
elif science<=49:
    science_grade= "F"
else:
    print(f"{science} invalid marks")

if english<=100 and english>=90:
    english_grade= "A"
elif english<=89 and english>=80:
    english_grade= "B"
elif english<=79 and english>=70:
    english_grade= "C"
elif english<=69 and english>=60:
    english_grade= "D"
elif english<=59 and english>=50:
    english_grade= "E"
elif english<=49:
    english_grade= "F"
else:
    print(f"{english} invalid marks")

print(f"maths marks-{maths}: maths grade-{maths_grade}")
print(f"science marks-{maths}: maths grade-{science_grade}")
print(f"english marks-{english}: maths grade-{english_grade}")

'''5. Write a program to check if a number is divisible by both 5 and 11
Python Programming'''

number=20
if number%5==0 and number%11==0:
    print(f"{number} is divisable by both 5 and 11")
else: 
    print(f"{number} is not divisible by 5 and 11")

# Loops
#1. Print numbers from 1 to the given number N
N=int(input("enter a number to get numbers: "))
i=0
while i<N:
    i=i+1
    print(i)






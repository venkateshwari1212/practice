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
# N=int(input("enter a number to get numbers: "))
# i=0
# while i<N:
#     i=i+1
#     print(i)

#2. Print even numbers up to the given number N
# num=int(input("enter a number to get numbers: "))
# i=0
# while i<num:
#     i=i+2
#     print(i)

# 3.Sum of first N natural numbers (sum = n * (n+1) / 2)
# number1=10
# i=1
# sum=0
# while i<=number1:
#     sum=sum+i
#     i=i+1
# print(sum)

#  Calculate the factorial of a number (n! = n × (n-1) × ... × 1) without using def function 4.
num2=5
i=5
factorial=1
while i>=1:
    factorial=factorial*i
    i=i-1
print(factorial)

# Print multiplication table of a number  Example:
#  2*1 = 2
#  2*2 = 4
num3=2
i=1
mul=0
while i<=10:
    mul=num3*i
    print(f"{num3}*{i}={mul}")
    i=i+1

# strings
# 1.Write a program to Reverse a given string (at least 2 ways)
user_input= "samjavaragamana"
reverse1=user_input[::-1]
print(reverse1)
reverse2=reverse1[::-1]
print(reverse2)

# 2. Count the number of vowels in a string
name= "venkateshwari"
count= 0
vowels="aeiouAEIOU"

for char in name:
    if char in vowels:
        count=count+1
print(count)

# Check if a string is a palindrome
poly= "jalaj"

rev_1=poly[::-1]
print(rev_1)
rev_2=rev_1[::-1]
print(rev_2)

if rev_1==rev_2:
    print("input is ployndrome")
else: 
    print("input is not polyndrome") 

string = "santoor"
# First reversal using a loop
reversed_string1 = ""
for char in string:
    reversed_string1 = char + reversed_string1  # Prepend each character
print("First Reversed String:", reversed_string1)

# second reversal using while loop 
reversed_string2=""
i=len(reversed_string1) - 1 
while i>=0 :
    reversed_string2= reversed_string2+ reversed_string1[i]
    i=i-1
print("second reversed string:",reversed_string2)


#  4.Convert uppercase to lowercase and vice versa
string1="can we join for DINNER?"
converted_text= string1.swapcase()
print(converted_text)

# using loop uppercase to lowercase and vice versa
converted_text1=""
for char in string1:
    if char.islower():
        converted_text1=converted_text1+char.upper()
    elif char.isupper():
        converted_text1=converted_text1+char.lower()
    else: 
        converted_text1=converted_text1+char
print(converted_text1)

# 5. Find the length of a string without using len() function
string2="Double choco chip"
count=0
for i in string2:
    count=count+1
print(count)
    

# lists
# 1.find the largest element of a list
l1=[300,450,202200,456,672]
largest=l1[0]
for num in l1:
    if num>largest:
        largest=num
print(largest)
# by using method
l1.sort(reverse=True)
print(l1[0])

# 2.find the smallest element in list 
l2=[10908,2098,240,54326,100,70]
smallest=l2[0]
for num in l2:
    if num<smallest:
        smallest=num
print(smallest)
# by using method
l2.sort()
print(l2[0])

# 3. Find the sum of elements in a list
# l3=[200,450,350,100]
# sum=0
# for num in l3:
#     sum=num+sum
# print(sum)

# # using while loop 
# sum1=0
# i=len(l3)-1
# while i >=0:
#     sum1=sum1+l3[i]
#     i=i-1
# print(sum1)

#  Sort a list in ascending order
l4=[2,50,100,123,000,209]
l5=["banana","apple","kiwi","orange","water melon","pineapple"]
l4.sort()
l5.sort()
print(l4)
print(l5)


# Remove duplicates from a list
l6=[800,20,50,30,50,90]
unique=[]
for num in l6:
    if num not in unique:
        unique.append(num)
print(unique)

# tuple
# 1 Find the maximum and minimum number in a tuple.
numbers = (200, 205, 303, 576, 8099, 20453)

max1 = numbers[0]
min1 = numbers[0]

for num in numbers:
    if num > max1:
        max1 = num  # Update max value
    if num < min1:
        min1 = num  # Update min value

print("Maximum value:", max1)
print("Minimum value:", min1)

# using methods
t1 = (10, 25, 3, 56, 89, 2)

# Find maximum and minimum
max_value = max(t1)
min_value = min(t1)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

# 2 Convert a tuple to a list
l7=list(numbers)
print(l7)

# 3 Count occurrences of an element in a tuple
t = (1, 2, 3, 4, 2, 2, 5, 3, 1, 4, 4, 5, 5)
element = 2  
count=0
for item in t:
    if item == element:
        count += 1
print(f"{element} appears {count} times in the tuple.")

# using method 
t = (1, 2, 3, 4, 2, 2, 5, 3, 1, 4, 4, 5, 5)
count_2 = t.count(2)  # Count occurrences of 2
print(f"2 appears {count_2} times in the tuple.")

# 4 Find the index of an element in a tuple
t = (10, 20, 30, 40, 50)
index_30 = t.index(30)  
print(f"The index of 30 is: {index_30}")

# 5 Reverse a tuple







#  Create a dictionary and print keys & values 1.
menu={
    "soup":["tomato soup","hot and sour soup"],
    "starter": ["fried chicken","bangla chicken","mutton maraag"],
    "main_course":["chicken biryani","rayudu pulav","mutton biryani"],
    "dessert":"sheer kurma"
}
# print(menu)
print(menu["soup"])

# 2 Find the sum of dictionary values 
prasad={
    "maths":99,
    "science":94,
    "social":98,
    "ebnglish":80
}
sum_prasad=0
for values in prasad.values():
    sum_prasad=sum_prasad+values

print(sum_prasad)

#using method:
sum_prasad1=sum(prasad.values())
print(sum_prasad1)

# Merge two dictionaries
jyothi={
    "math":99,
    "sci":54,
    "soc":98,
    "eng":80
}
exam={**prasad,**jyothi}
print(exam)

# my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sorting by values using sorted() and lambda
sorted_dict = dict(sorted(jyothi.items(), key=lambda item: item[1]))

print(sorted_dict)

# using prasad dict for sorting
# Convert dictionary to a list of (key, value) pairs
items = list(prasad.items())
n = len(items)

# Bubble Sort
for i in range(n - 1):
    swapped = False  # Track if swaps happen

    for j in range(n - 1 - i):
        if items[j][1] > items[j + 1][1]:  # Compare values
            items[j], items[j + 1] = items[j + 1], items[j]  # Swap
            swapped = True

    if not swapped:
        break  # Stop if already sorted

# Convert the sorted list back to a dictionary
sorted_dict = dict(items)

# Print sorted dictionary
print("Sorted dictionary:", sorted_dict)


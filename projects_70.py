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




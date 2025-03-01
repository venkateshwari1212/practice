# Boolean Values
# bollean values will return output as true or false 
print(10>5)
print(10==3)
print(9<7)
# nothing to commit
# conditional statement using boolean
a=2000
b=20
if a/b==0:
    print("a is a even number")
else:
    print("a is an odd number")

print(bool("hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
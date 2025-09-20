# Arithmetic Operators

a = 34
b = 67
c = a + b
print(c)


# Assignment Operators

a = 45 - 32  # Assigns 45 - 32 in 'a'
print(a)
b = 6
# b += 3 # Increament the value of 'b' by 3 (6 + 3 = 9) and assign it to b
# b -= 3 # Decrement the value of 'b' by 3 (6 - 3 = 3) and assign it to b
b *= 3  # Multiply the value of 'b' by 3 (6 * 3 = 18) and assign it to b
print(b)


#Comparison Operator (Return value is always boolean)

d = 5 > 4 # If 5 is greater, then true else false
print(d)
e = 45 < 32 # False
print(e) 
f = 5 >= 5 # True
print(f)
g = 45 != 56 # "! = Not Equal to"
print(g)
h = 5 == 5 # "== mean is 5 equal to 5"
print(h)


# Logical Operators

# Truth Table for 'OR': (Output Depend on Following)
# True + True = True 
# True + False = True
# False + True = True
# False + False = False

i = True or False
j = False or False
print (i)
print (j)

# Truth Table for 'AND': (Output Depend on Following)
# True + True = True 
# True + False = False
# False + True = False
# False + False = False

k = True and False
print(k)

#Truth Table for 'NOT':
# True = False
# False = True

print(not(False))
print(not(True))
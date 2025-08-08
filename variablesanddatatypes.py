# INTRODUCTION TO PYTHON
# Contents covered : Variables , Data types , Input/Output , Operators

# How to Display Output
print("Hello World")
print("I like coding in 'python' language.")
print("My name is Niharika," , "I am 25 years old.")
print(35+25)

# Variables
name = "Niharika"
age = 35
print("My name is" , name)
print("My age is", age)
price = 35.56
print("The cost of this pen is" , price)

# Storing one variable's data to another variable
age1 = age
print (age1)

# How to get data type of any variable/identifier
a = True
b = None
print("The data type of the 'name' variable is:" ,type(name))
print("The data type of the 'age' variable is:" ,type(age))
print("The data type of the 'price' variable is:" ,type(price)) 
print("The data type of the 'a' variable is:" ,type(a))
print("The data type of the 'b' variable is:" , type(b))

# Aritmetic Operators
a= 10
b = 5
print("Sum of two numbers: " , (a+b))
print("Difference of two numbers: " , (a-b))
print("Product of two numbers: " , (a*b))
print("Quotient of two numbers: " , (a/b))
print("Remainder of two numbers: " , (a%b))
print("a power b : " , (a**b))

# Relational/Comparison Operators -----> Always return the boolean value
a = 2
b = 5
print("a = 2 and b = 5")
print("Is a == b ? : " , (a == b))
print("Is a != b ? : " , (a != b))
print("Is a <= b ? : " , (a <= b))
print("Is a >= b ? : " , (a >= b))
print("Is a < b ? : " , (a < b))
print("Is a > b ? : " , (a > b))

# Assignment Operators
a = 2
a += 2
print ("+= operator for a=2 : " , a)
a -= 2
print ("-= operator for a=2 : " , a)
a *= 2
print ("*= operator for a=2 : " , a)
a /= 2
print ("/= operator for a=2 : " , a)
a %= 2
print ("%= operator for a=2 : " , a)

# Logical Operators -----> Works on boolean values
a = 50
b = 100
print("For a = 50 and b = 100")
print("(a<b) AND (b>a) :" , (a<b) & (b>a))
print("(a<b) AND (b<a) :" , (a<b) & (b<a))
print("(a<b) OR (b<a) : " , (a<b) | (b<a))
print("NOT(a<b): " , not(a<b))
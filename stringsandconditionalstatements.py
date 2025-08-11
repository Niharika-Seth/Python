# How to define a string
str1 = "This is a string. "
str2 = 'This is a string.'
str3 = """This is a string."""
print(str1)
print(str2)
print(str3)

# Why we use double quotes and triple quotes?---> In order to use single quotes inside it.
str = "My name is 'Niharika Seth'."
print(str)

# Escape Sequence Characters ----> \n , \t
ab = "My domain is AI & DS.\nI like coding in python and learning different algorithms."
print(ab)

bc = "My domain is AI & DS.\t\tI like coding in python and learning different algorithms."
print(bc)

# String Operations
# Concatenation -----> to join 2 strings using + operator
a = "My name is Niharika Seth."
b = "I am 20 years old."
c = "My passion is reading and researching in the domain of Quantum Physics."
print(a +" "+ b +" "+ c)

# Length of String ----> to find length of the string
d = len(a)
print("The length of string a is:" , d)
print("The length of string b is:" , len(b))
print("The length of string c is: " , len(c))

# Indexing -------> Position of characters in a string
stra = "Python Language"
s = stra[0]
p = stra[1]
q = stra[-1]
r = stra[6]
print(s+p+q+r)

# Slicing -----> Accessing parts of a string
strb = "Glass of Water"
n1 = strb[1:7]
n2 = strb[:10]  # is equals to strb[0:10]
n3 = strb[2:]
n4 = strb[6:len(strb)]
n5 = strb[:-1]
n6 = strb[-5:]
n7 = strb[-8:-14]
print (n1)
print(n2)
print(n3)
print(n4)
print(n5)  
print(n6)
print(n7)
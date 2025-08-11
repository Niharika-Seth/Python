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

# String Functions
# endswith() function ----> to check if the string ends with given substring
strc = "computer vision"
print("Is the string ending with on? : " , strc.endswith("on"))
print("Is the string ending with eh? : " , strc.endswith("eh"))

# capatalize() function ----> capitalize the 1st character of a string
print(strc.capitalize())

# replace() function ----> to replace old substring with new substring
strd = "I like python programming language"
print("Replacing i with w :  " , strd.replace("i" , "w"))
print("Replacing python with java: " , strd.replace("Python" , "Java"))

# find() function ----> to search for the word in a string and if the word exist it returns the index of its first occurence
print("Python word in the string : " , strd.find("Python"))
print("i in the string: " , strd.find("i"))
print("I in the string: " , strd.find("I"))
print("Letter q in a string: " , strd.find("q"))   # returns -1 as it doesnt exist in the string , negative index is only valid for slicing 

# count() Function
print("The letter 'a' in a string: " , strd.count("a"))
print("The word python in a string : " , strd.count("python"))

# WAP to input user's first name and print it's length
a = input("Enter your first name: ")
print("The length of your first name is : " , len(a))

# WAP to find the occurences of '$' in a string
b = "hi , $i am the $ symbol , $my name is $99.69"
print("The occurence of $ in a string is: " , b.count("$"))

# Conditional Statements 
# Synatx ----> predefined rules or standard way for programming
# If-elif-else statement  ---> if statement will always be checked but the elif statemnet will only be checked if "if" statement is false.
temp = int(input("Enter temperature of your location: "))
if (temp <= 10):
  print("The climate is very cold.")
elif (temp <= 30):
  print("The climate is sunny.")
else:
  print("The climate is very hot.")

# if-else statement
light = input("Enter the signal light (green or red): ")
if (light == "red"):
  print("Stop the vehicle.")
else:
  print("Start the vehicle.")

# WAP to grade students based on marks
m = int(input("Enter student's marks: "))
if (m >= 90):
  print("GRADE A")
elif (90 > m >= 80):
  print ("GRADE B")
elif ( 80 > m >= 70):
  print ("GRADE C")
else:
  print ("GRADE D")

# Nested statements ----> statement within a statement
age = int(input("Enter age: "))
if (age >= 18):
  if (age >= 21):
    print("You can drink.")
    print("You can drive.")
else:
  print("You are neither allowed to drink nor drive.")

# WAP to check if the number entered by user is odd or even.
n = int(input("Enter the number: "))
if ( n%2 == 0):
  print(f"{n} is an Even Number.")
else:
  print(f"{n} is an Odd Number.")

# WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if (num1 > num2 and num1 > num3):
  print(f"{num1} is the greatest number.")
elif (num2 > num1 and num2 > num3):
  print(f"{num2} is the greatest number.")
else:
  print(f"{num3} is the greatest number.")

# WAP to check if a number is a mutiple of 7 or not
num = int(input("Enter your number: "))
if (num%7 == 0):
  print(f"{num} is divisible by 7.")
else:
  print(f"{num} is not divisible by 7.")




 



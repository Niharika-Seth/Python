# How to define a function -----> block of statement that performs a specific task. It can be called several times to perform the same task.  
def cal(a , b):         # function definition and (a,b) are parameters
  return a + b

x = int(input("Enter first number: "))    # input
y = int(input("Enter second number: "))   # input
c = cal (x,y)  # x and y are arguments and this is function call
print(f"The sum of {x} and {y} is: ", c)

def display():
  x = print ("hello")
  return x

print (display())

# WAP to create function to calculate average of 3 numbers.
def average(x,y,z):
  sum = x+y+z
  avg = (sum/3)
  return avg
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = average(a,b,c)
print(f"The average of {a} , {b} and {c} is : " , d)

# Built-in Functions ----> Some pre-defined functions available in python.
# print() function with end = " " as argument. end = " " decide what the sentence should end with.
print("Hello World" , end = " ")
print("My name is Lara.")

# len()
a = "DATA SCIENCE"
print(len(a))

# range()
for i in range(1 , 11):
  print (i)

# type()
a = 23
print(type(a))




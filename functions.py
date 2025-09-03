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

# In default parameters , non default arguments come first and then default argument comes.
# For instance : def sum (a = 2 , b): ---> will throw error but def sum(a , b = 2): ----> will not throw any error.

# User Defined Functions

# WAF To print the length of a list. (list is the parameter)
l = [1,2,3,4,5,6,7,8,9,10]
n = ["mumbai" , "kolkata" , "delhi" , "noida" , "kerela"]
def len_of_list(list):
  a = len(list)
  return a
print("The length of list l is: " , len_of_list(l))
print("The length of list n is: " , len_of_list(n))

# WAF To print the elements of list in a single line. (list is a parameter)
cities = ["MUMBAI","KOLKATA","DELHI","NOIDA"]
cars = ["Porsche" , "Lamborghini" , "BMW","Mercedes","Ferrari","McLaren","Apollo"]
def display_list(l):
  return (print(l))
print("The element of the list 'cities' are: " , display_list(cities))
print("The element of the list 'cities' are: " , display_list(cars))

# WAF to find factorial of n. (n is the parameter)
def fact(n):
  i = 1
  fact = 1
  for i in range (1,n+1):
    fact = fact * i
    i +=1
  return (fact)
a = int(input("Enter the number to find its factorial: "))
b = fact(a)
print(f"The factorial of {a} is: " , b)

# WAF to convert USD TO INR
def convert_usd_inr(a , b = 88.6):
  inr = a * b
  return(inr)
x = int(input("Enter USD value : "))
y = convert_usd_inr(x)
print(f"The INR value of {x} is: " , y)

# WAF to check whether the given number is odd or even.
def even_odd(n):
  if (n%2 == 0):
    print(f"{n} is an even number.")
  else:
    print(f"{n} is an odd number.")
a = int(input("Enter your number: "))
even_odd(a)



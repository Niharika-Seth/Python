# Loops ----> Used to repeat instructuions

# While Loop ----> while condition is true , execute statement inside the while loop.
# Print Hello world 10 times using while loop
i = 1
while (i <= 100):
  print(("Hello World" , i))
  i += 1

# Print numbers 1 to 5
i = 1
while (i <= 5):
  print (i)
  i += 1

# Print numbers 5 to 1 
i = 5 
while ( i >= 1):
  print(i)
  i -= 1

print ("Loop Ended")

# WAP to print numbers from 1 to 100
i = 1
while (i <= 100):
  print(i)
  i += 1
print ("Loop Ended")

# WAP to print numbers from 100 to 1
i = 100
while (i >= 1):
  print (i)
  i -= 1
print ("Loop Ended")

# WAP to print the multiplication table of a number n
n = int(input("Enter the number: "))
i = 1
print (f"The table of {n} is given as follows: ")
while (i <= 10):
  print (f"{n} * {i} = ", n*i)
  i += 1
print("Loop Ended")

# WAP to print the elements of the following list using loops: [1,4,9,16,25,36,49,64,81,100]
l= []
i = 1
while(i <= 10):
  l.append(i * i)
  i += 1
print(l)

# Search for a number x in this tuple using loops: [1,4,9,16,25,36,49,64,81,100]
t = (1,4,9,16,25,36,49,64,81,100,25)
x = int(input("Enter the number you want to search in the tuple: "))
i = 1
while (i <= 10):
  if (x == t[i]):
    print(f"{x} is found at index {i}")
  else:
    print(f" Finding {x} ...")
  i += 1

# Break Keyword ----> used to terminate the loop when encountered
i = 1
while(i <= 5):
  print(i)
  if (i == 4):
    break
  i += 1
print("End of loop")

# Continue Keyword ----> terminates execution in the current iteration and continues execution of the loop with the next iteration.
i = 0
while (i <= 10):
  if (i == 5):
    i += 1
    continue
  print(i)
  i += 1
print("End of loop")

# WAP to skip even numbers and print only odd numbers
n = int(input("Enter your number: "))
i = 1
while (i <= n):
  if (i%2 == 0):
    i += 1
    continue
  else:
    print(i)
  i += 1

# WAP to skip odd numbers and print only even numbers
n = int(input("Enter your number: "))
i = 1
while (i <= n):
  if (i%2 != 0):
    i += 1
    continue
  else:
    print(i)
  i += 1

# For Loop ----> used for sequential traversing in list , tuples , strings etc
l = [1,2,3,4,5]
for num in l:
  print (num)

a = ["Python" , "Java" , "R", "SQL" ,"C","C++" ,"C#"]
for lang in a:
  print(lang)

b = "Niharika Seth"
for char in b:
  print(char)
else:
  print("End")

# WAP to print the elements of the following list using for loops: [1,4,9,16,25,36,49,64,81,100]
c = [1,4,9,16,25,36,49,64,81,100]
for el in c:
  print(el)
  
# WAP to search for a number x in this tuple using for loop: [1,4,9,16,25,36,49,64,81,100]
d = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter Number you want to search in the tuple: "))
for el in d:
  if (x == el):
    print(f"{x} is found at index {i}.")
    break
  else:
    print(f"Finding {x} ...")

# Range() function ----> Returns a sequence of a numbers , starting from zero by default and increments by 1 (by default) and stops before a specified number.
# range(stop)
for i in range(10):
  print(i)

# range(start,stop)
for i in range (2,11):
  print(i)

# range(start,stop,step)
for i in range(10,110,10):
  print(i)

# WAP to print even numbers from 1 to 100 using range function
for i in  range(0,101,2):
  print(i)

# WAP to print numbers from 1 to 100 using for loop and range function
for i in range (1,101):
  print(i)

# WAP to print numbers from 100 to 1 using for loop and range function
for i in range (100,0,-1):
  print(i)

# WAP to print the multiplication table of a number n.
n = int(input("Enter your number: "))
for i in range(1, 11):
  print(f"{n} * {i} = " , n*i)

# Pass Statement ----> It is a null statement that does nothing. It is used as a placeholder for future code.
for i in range(5):
  pass
print("LEFT PLACE FOR SOME USEFUL WORK")

# WAP to find the sum of first n numbers using while loop.
n = int(input("Enter your number: "))
i = 0
sum = 0
while (i <= n ):
  sum = sum + i
  i += 1
print(f"The sum of first {n} numbers is {sum}.")

# WAP to find the factorial of first n numbers using for loop
n = int(input("Enter number to find factorial: "))
i = 1
fact = 1
for i in range(1,n+1) :
  fact = fact * i
  i += 1
print(f"The factorial of {n} is {fact}.")
  

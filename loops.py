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

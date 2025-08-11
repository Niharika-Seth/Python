# How to define tuples 
t = (1,2,3,4,'python',3,4,5,5,5,5)
print(t)
print("the data type of t is: " , type(t))

# Tuples are immutable built in data type that stores values of different data types together.
# To create a tuple with single value always add , at the end of the element. (with multiple values , is optional)
a = (1,)
print("The data type of a is: " , type(a))

# To access elements of tuple
print("The element at 1 index: " , t[1])
print("The element at 4 index: " , t[4])

# Tuple slicing -----> similar to list slicing
print(t[0:])
print(t[1:4])
print(t[:4])
print(t[:-1])
print(t[-1:])
print(t[-4:-1])

# Tuple Methods
# index(ele) function ----> returns index of first occurence of element
print("The index of first occurence of '5' element is: " , t.index(5))

# count(ele) function -----> it counts the total occurences of an element
print("The number of times '5' element has occured : " , t.count(5))
print("The number of times '4' element has occured : " , t.count(4))
print("The number of times '3' element has occured : " , t.count(3))
print("The number of times '2' element has occured : " , t.count(2))

# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
movies=[]
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))
print(movies)

# WAP to check if a list contains a palindrome of elements.
n1 = ["r","a","d","a","r"] 
copy_n1 = n1.copy()
copy_n1.reverse()
if (n1 == copy_n1):
  print(f"{n1} is Palindrome.")
else:
  print(f"{n1} Not Palindrome.")

# WAP to count the number of students with the "A" grade in the following tuple
t = ("C","D","A","A","B","B","A")
print("The number of students with 'A'grade are: " , t.count("A"))

# Store the above values in the list and sort them from "A" to "D".
list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)
list.sort(reverse = True)
print(list)




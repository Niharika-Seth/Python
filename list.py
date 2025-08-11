# How to define List
l = [23,34,5,6,67,8,88]
print (l)
print("Data type of l : " , type(l))

# To access items from the list
print("The number at index 0  : " , l[0])
print("The number at index 1 : " , l[1])
print("The number at index 4 : " , l[4])

# To print length of the list (same as string)
print("The length of the list is : " , len(l))

# List can store different types of data together while arrays can store only one type of data. 
# List can be mutable but strings are immutable.

# To replace old value with new value in list (mutable)
l[0] = "Python"
print(l)

# List Slicing ----> similar to string slicing
print(l[0:3])
print(l[:6])
print(l[:-2])
print(l[1:])
print(l[-4:-1])
print(l[-6:])

# List Methods 
# append() function ---> enter elementat the end of the list
a = ["python" , "java" , 23, 45, 69, 23, 67]
a.append("c++")
print(a)

# Sorting is possible with characters also based on which letter comes first
# sort() function ----> arrange the list is ascending order 
b = [23,34,56,1,78,90,50]
b.sort()
print (b)

# sort(reverse = True) function ----> sorts the list in descending order
b.sort(reverse = True)
print(b)

# reverse() function ----> reverse the order of list
a.reverse()
print(a)

# insert(index , element) function ----> inserts the element at particular index
n = ["python" , 1 ,2, 3, "java"]
n.insert(2 , 22)
print(n)

# remove(element) function ----> removes the first occurence of a element
p = [1 , 2, 3, 4, 5, 3, 9,10 , 11 ,15, 12 , 11]
p.remove(11)
print(p)

# pop(index) function ----> removes the element of particular index
p.pop(5)
print(p)

# count() function ----> it counts the occurence of a particular element
print("The occurence of '11' elements is: " , p.count(11))


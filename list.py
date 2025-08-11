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


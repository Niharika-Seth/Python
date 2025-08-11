# How to define sets----> elements of set are immutable but set is mutable
s = {1,2,3,4,5,"python","java",4}
print(s)
print("The data type of set is : " ,type(s))

# set ignores duplicate items
print("The length of set: " , len(s))

# To create empty sets
sets = set()
print(type(sets))

# Set methods
# add() function ----> add an element
a = {1,2,3,4}
a.add(7) 
a.add("python")
print(a)

# remove() function ----> removes an element from the sets
a.remove(1)
print(a)

# pop() function ----> removes random element from the set
a.pop()
print(a)

# clear() function ---> empties the set
a.clear()
print (a)

# union(s2) function ---> combines both the set's values and return new one
b = {1,2,3,4,5,6,7,8}
c = {1,2,3,89,"python" , "java"}
print("Set B union C: " , b.union(c))

# intersection(s2) ----> returns the common values from both sets
print("Intersection of both sets: " , b.intersection(c))

# QUE 1
dict = {
  "cat" : "a small animal",
  "table" : ["a piece of furniture" , "list of facts and figures"]
}
print(dict)

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. use subject name as key and marks as value.
stud = {}
x = int(input("Enter the marks of Physics: "))
stud.update({"Physics" : x })
y = int(input("Enter the marks of Biology: "))
stud.update({"Biology" : y})
z = int(input("Enter the marks of Chemistry: "))
stud.update({"Chemistry" : z })
print(stud)


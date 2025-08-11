# How to define dictionary 
info = {
  "Name" : "Niharika",
  "Age" : 23,
  "Domain" : "AI & DS"
}
print(info)

# We can also store list or tuples in a dictionary (Key can only accept int,float,string, tuple data type and not list.)
dict = {
  "Name" : "Niharika",
  "Subjects" : ["Maths" , "Science" , "English" ,"Civil"],
  "Marks" : (50,85,99,79)
}
print(dict)
print("The data type of dict is: " , type(dict))

# To access information of dictionary
print(dict["Name"])
print(dict["Subjects"])
print(dict["Marks"])

# To change element of the dictionary 
dict["Name"] = "Lara"
print(dict)
dict["Age"] = 22
print(dict)

# To create empty dictionary
null_dict = {}
print("The data type of null_dict: " , type(null_dict)) 

# Nested Dictionary
stud = {
  "Name" : "Niha",
  "Subjects" : {
    "phy" : 55,
    "chem" : 67,
    "bio" : 90,
    "comps" : 99
  },
  "age" : 19
}
print(stud)
print(stud["Subjects"])
print(stud["Subjects"] ["comps"])

# Dictionary Methods
# keys() function ---> return all the keys of dictionary
print(dict.keys())

# To get total number of keys we use length function
print("Total number of keys in a dictionary : " , len(dict))

# values() function ----> return all the value of dictionary
print(dict.values())

# items() ----> returns all the key:value pairs in form of tuples
print(dict.items())

# get("key") function ----> returns the key according to the value. (.get() does not throw error)
print(dict.get("Subjects"))
print(dict.get("Marks"))

# update({new_dict or key:value}) ----> insert the specified items to the dictionary
dict.update({"City" : "Mumbai"})
print(dict)
new_dict = {"Phone number" : 900468296, "DOB" : "22 July 2004"}
dict.update(new_dict)
print(dict)

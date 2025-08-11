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

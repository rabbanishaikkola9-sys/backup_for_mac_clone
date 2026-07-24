dict={
    "name": "rabbani",
    "name":"rehaan",
    "marks":100,
    "age":15,
    "li":[1,2,3,"rabbani",True]
}
print(type(dict),"\n",dict)
# List of key value pairs
print(dict["name"])
# print(dict["name1"])
print(dict["marks"])
print(dict["age"])
print(dict,"\n","The length of the dictionary is :",len(dict))
d={} # empty dictionary
print(type(d),d)
print(dict.get("aha",0))
# Python Dictionaries

dic = {
    1:"Sumit",
    2:"Sahil",
    3:"Harsh"
    }
print(dic[1])



#Accessing Dictionary Items

dict={
    "name":"Sumit",
    "age":18,
    "Eligible":True
    }

print(type(dict))

#print(dict["name1"])  # it will throw error because name1 dont exist

print(dict.get("name1")) #it will not throw error output will be NONE

print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(key)

for values in dict.values ():
    print(key)

for key in dict.keys():
    print(f"The value Corrresponding to the key {key}is {dict[key]}")

print(dict.items())
for key,values in dict.items():
     print(f"The value Corrresponding to the key {key} is {dict[key]}")


#updates Method
ep1={122:45,123:89}
ep2={222:67,223:70}
ep1.update(ep2)
print(ep1)

#clear Method
ep1.clear()
print(ep1)

#pop and popitem method
ep2.pop(222)
print(ep2)

ep2.popitem() #pop last item
print(ep2)

#Add
ep2.update({233:22})
print(ep2)

#delete
del ep2[233]
print(ep2)


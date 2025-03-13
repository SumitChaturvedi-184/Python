#code1   [truncate can only be done in w,r+ modes]
f = open("sample3.txt","w")

f.write("Hello Everyone")

f.truncate(3) #the truncate method is used to truncate a 
                     #file to a specific size

f.close()

f = open("sample3.txt","r")
print(f.read())
 
 #how truncate printed only 3 character as per specified size

f = open("sample3.txt","r+")

f.write("Hello Everyone")

f.truncate(3) #the truncate method is used to truncate a 
                     #file to a specific size

f.close()


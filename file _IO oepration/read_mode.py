f = open("Sumit1.txt","r")
txt = f.read()
print(txt)
f.close()

#or

with open("Sumit1.txt","r") as f:  #the with keyword automatically
   print( f.read())                # closes the file without specifying f.close()
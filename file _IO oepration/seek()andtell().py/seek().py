

f = open("sample2.txt","r")
print(type(f)) # it shows the inbuilt class name that includes seek and tell method in it

f.seek(12)  # used to skip mean seek value
#line = f.readline() #as it skiped 12 character including space and
#printed the left character after 12 characters

print(f.tell())#

line1 = f.readline(5)
#print(line)  

print(line1) #this will print only 5 character after
#the skipped or seeked character

f.close()
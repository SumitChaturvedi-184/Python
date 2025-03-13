f = open("sample2.txt","r")

print(f.tell()) #tell the current postion of the seeked or skipped charcter

f.seek(5) #after seeking 5 characters

print(f.tell()) 

f.close()
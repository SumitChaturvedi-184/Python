index = 0
f = open("sumit.txt","r")
while True:
    line=f.readline()
    index+=1
    if not line:
        break
    m1=int(line.split(" , ")[0])
    m2=int(line.split(" , ")[1])
    m3=int(line.split(" , ")[2])
    print(f"The marks for student {index} is : {m1*2}")
    print(f"The marks for stud-*ent {index} is : {m2*2}")
    print(f"The marks for student {index} is : {m3*2}")
   
    print(line)
f.close()
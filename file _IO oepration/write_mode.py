#write mode me ek baar hi likhta hai run karne pe 
# file ke start me aur repreat nahi karta jaise append
#  method me run pe click karo to print karta rahega


with open("Sumit1.txt","w") as f:
    f.write("Write operation sucessful")

with open("Sumit1.txt","w") as f:
    f.write("1 Write operation sucessful")  #ye update kardiya upper ke write ko

with open("Sumit1.txt","r") as f:
    print(f.read())
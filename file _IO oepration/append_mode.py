# isme last mein append karta rahega aur 
#repeat hote rahega wo text baar baar 

with open ("Sumit1.txt","a") as f:
    f.write("Hello World")

with open("Sumit1.txt","r") as f:
    print(f.read())
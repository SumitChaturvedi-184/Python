#Encoding

message = input("Enter The Message:")
words=message.split()
coding = input("Enter 1 for Coding and 0 for Decoding:")
coding=True if(coding=="1") else False
if(coding):
    text=[]
    for word in words:
        if (len(word)>=3):
            r1="lvd"
            r2="pwd"
            stnew = r1+word[1:]+word[0]+r2
            text.append(stnew)
        else:
            text.append(word[::-1])
    print(" ".join(text))
else:
    text=[]
    for word in words:
        if (len(word)>=3):
            stnew=word[3:-3]
            stnew = word[-1]+word[:-1]
            text.append(stnew)
        else:
            text.append(word[::-1])
    print(" ".join(text))
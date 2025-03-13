#Encoding

message = input("Enter The Word:")
words=message.split(" ")
coding=int(input("Enter 1 for Coding and 2 for Decoding:"))
coding=True if(coding==1) else False
print(coding)
if(coding):
    text=[]
    for word in words:
        if (len(word)>=3):
            r1="dxy"
            r2="trp"
            strnew=r1+word[1:]+word[0]+r2
            text.append(strnew)
        else:
            text.append(word[::-1])
    print(" ".join(text))
else:
    text=[]
    for word in words:
        if (len(word)>=3):
            str=word[3:-3]
            strnew=str[-1]+str[:-1]
            text.append(strnew)
        else:
            text.append(word[::-1])
    print(" ".join(text))

    

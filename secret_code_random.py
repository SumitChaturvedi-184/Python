import random

message = input("Enter The Message:")
words = message.split()
coding = int(input("Enter 1 for Coding or 0 For Decoding:"))
coding=True  if(coding==1) else False
if(coding==True):
    text=[]
    sample = "abcdefghijklmnopqrstuvwxyz"
    for word in words:
        if (len(word)>=3):
            r1=''.join(random.choices(sample,k=3))
            r2=''.join(random.choices(sample,k=3))
            newtxt=r1+word[1:]+word[0]+r2
            text.append(newtxt)
        else:
            text.append(word[::-1])
    print(" ".join(text))

else:
    text=[]
    for word in words:
        if (len(word)>=3):
            newtxt=word[3:-3]
            newtxt=newtxt[-1]+newtxt[:-1]
            text.append(newtxt)
        else:
            text.append(word[::-1])
    print(" ".join(text))


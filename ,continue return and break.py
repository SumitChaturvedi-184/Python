#Break keyword is used to break the loop
'''
def br():
    for i in range(0,10):
        if (i==3):
            break
            print("Hello")
    print("loop breaked")
br()
'''

#continue keyword is used to end the 
#current iteratioin of the loop and 
#and continue next iteration

'''
def co():
    for i in range(0,5):
        if (i==3):
            continue
        print(i)
    #print("loop breaked")
co()
'''


#Return Keyword

def re():
    index=1
    for i in range(5):
        results=index+i
        return results
        
print(re())




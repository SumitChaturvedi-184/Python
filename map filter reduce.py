l = [2,4,6,8,10]

#map
def sqaure(n):   #map applies a given function to each item of 
    return n*n   #an iterable (like a list) and returns a map object (which is an iterator).
print(sqaure(2))

newl=[]

newl = map(sqaure,l)
print(list(newl))


#----Filter---- 
#filter applies a given function to each item of an iterable and returns 
# a filter object (which is an iterator) containing only the items for which the function returns True.
def check(x):
    return x>2
print(check(1))


newl1 = filter(check,l) # it checks all the elemnt in the list and 
print(list(newl1))     #return the number from the list that are bigger 
                        #than 2 


# reduce

from functools import reduce     #The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements
                                 #mentioned in the sequence passed along.This function is defined in “functools” module
l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))   






#lambda functions are anonymus function with without a name
#lambda function are often used in situation where 
# small function is required for a short time


#def sum(x,y):
 #   return x+y
#print(sum(2,3))

# or Using lambda function now


#lambda function should obly be used for 
#1 line and small function like below
#for multiple line lambda fuctio is not 
#suitable.

variable = lambda x,y: x+y
print(variable(3,4))

cube = lambda x:x*x*x
print(cube(2))

avg = lambda x,y,z:(x+y+z)/2
print(avg(2,3,4))


# creating a function and calling a function as a parameter in it

# 1)
square = lambda x:x*x  #here i declared the 1st function square

def cube(square,value): #passing the square function here as an argument
    return 5+square(value)


print(cube(square,2)) #caling function with it paramter values

#2)
square = lambda x:x*x  #here i declared the 1st function square

def cube(fx,value): #passing the square function here as an argument
    return 5+fx(value)


print(cube(square,2)) #caling function and passing values for the argument 
#here i passed square as an value for the parameter argument





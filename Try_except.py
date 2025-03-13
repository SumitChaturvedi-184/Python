# syntax error 
'''''
try:
    print(Hello World)
except SyntaxError:
    print("There is an error in Syntax")

try:
    print(This is not valid Python)  # This will raise a SyntaxError
except SyntaxError:
    print("There's a syntax error in your code. Please check for missing colons or parentheses.")
'''

#TypeError

try:
    name="Sumit"
    age=21
    total_age = name + age
except TypeError:
    print("You can not add string to integer")


#NameError

try:
    print(Greeting)
except NameError:
    print("You are trying to use variable before assigning ")


#IndexError

try:
    fruits = ["apple","banana"]
    print(fruits[2])
except IndexError:
    print("The index is out of list range")


#Keyerror

try:
    person = {"name":"Bob","age":30}
    print(person["City"])
except KeyError:
    print("The key you're using doesn't exist")


#Valueerror

try:
    number = "ten"
    converted_number = int(number)
except ValueError:
    print("The value you're trying to convert cannot be converted to desired datatype")


#AttributeError

try:
    text = "Hello"
    print(text.split())
except AttributeError:
    print("The object you're using doesn't have the method")


#OSError

try:
    with open("Data.txt","w") as file:
        data = file.read()
except OSError:
    print("There's an error in opening or reading the file")


#ZeroDivisionError

try:
    result = 10/0
except ZeroDivisionError:
    print("You can't divide by zero")


#importError
try:
    import nonexistingmodule
except ImportError:
    print("The module does not exist")

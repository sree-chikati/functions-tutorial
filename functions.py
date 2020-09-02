#def tells Python that you are about to define a function. 
#def is followed by the name of the function and the parameters are put inside parentheses ( ) and separated by commas. 
#Indented under the function name is the action code (or code block) that does something to process the parameters.
#Finally in order to get the result the function must return something using the return keyword. 

def area(width, height):
    result = width * height
    return result

#To use a function we have defined we need to "call" the function. 
#To call a function you write the function name followed by parentheses and then you provide values to the function inside the parentheses like below:
result = area(5, 6)
print(result)

#instead of calling strong new values in the variable "result"
#all the time, you can directly store the values in the print function too
result = area(4,5)
print(result)
print(area(3, 5))


def subtract(num1, num2):
    result = num1 - num2
    return result

print(subtract(20, 10))
print(subtract(30, 10))


def divide(num1, num2):
    result = num1 / num2
    return result

print(divide(20, 2))
print(divide(99, 9))


def add(num1, num2):
    result = num1 + num2
    return result

print(add(3, 2))
print(add(20, 40))
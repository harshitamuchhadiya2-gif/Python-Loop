#what is function?
#A function is a block of code that runs only when it is called

#why use function?
#1. Avoid repeating code
#2.Makes program clean & organize
#3. Easy to debug and reuse

#...........................................................................................

#syntax:
#def function_name():
   #code

#example:
def greet():
    print("Hello Students")
greet()

#.......................................................................................

#function with parameters
#used to pass values

def greet(name="Student"):
    print(f"Hello {name}")
greet()
greet("sonal")
greet("krupa")

#...........................................................................................

#functon with Return values
#used when we want to send result back 
def add(a,b):
    return a+b
result = add(2,3)
print(result)

#..............................................................................................

#task 1 - create a calculator and retuen result








#task 2 - create a function to check if a number is even or odd
#userdefine
num = int(input("Enter a number: "))
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
result= check_even_odd(num)
print(result)

#task 3 - create a function to find the factorial of a number
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* fact (n - 1)
num = int(input("Enter a number: "))
result = fact(num)
print(result)


#task 4 - create a function to find maximum and of three number
def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("Enter a number: "))
result = find_max(a,b,c)
print(f"The Greatest number is : {result}")    

#task 5 - create a function to check if a strin is palindrom
def is_palindrom(s):
    return s == s[::-1]
input_str = input("Enter a string: ")
result = is_palindrom(input_str)
if result:
    print(f"{input_str} is a palindrom")
else:
    print(f"{input_str} is not a palindrom")

#task 6 - create a function to calculate the area of a circle
def area_of_circle(radius):
    return 3.14 * radius ** 2
redius = float(input("Enter radius of circle"))
area = area_of_circle(redius)
print("the area of circle is : {area}")
 

# #what is a loop?
# #A loop is used to reapet a block of code multiple times until a condition is met

# #types of loops in python
# #1. for loop
# #used when we know how many times we want to repeat 

# #synatx:
# #for variable in sequence:
# #     # code


# #range() function is commonly used to generate a sequence of numbers.

# #range comes with 3 parameters
# #1. start(inclusive)
# #2. stop(exclusive)
# #3. step(ooptional,default is 1)

# #range(start,stop-1,step)

# #example:
# for i in range(1,6):
#     print(i)


# #key points:
# #1. range(start,stop)generates numbers
# #2. loop runs fixed mu,ber of times

# #.......................................................................................................

# # 2.While loop  - Used when we repeat until a condition becomes False
# # Syntax:
# # while condition:
# #     code

# i = 1
# while i <= 5:
#     print(i)
#     i += 1 #op:1 2 3 4 5
# # Key points:

# # Loop control Statement

# # 1.Break - Stop the loop immediately 
# # Example
# for i in range(1,6):
#     if i == 3:
#         break
#     print(i) #op:1 2

# # 2. Continue - Skip current iteration 
# # Example
# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i) #op:1 2 4 5

# # Pass - Does nothing(placeholder)
# for i in range(5):
#    pass #op:1 2 3 4 5 

# # Task 1 - Print numbers from 1 to 10 using for loop.
# for i in range(1 , 11):
#     print(i)

#task 2 - print even numbers from 1 to 20
# for i in range(1,21):
#     if i % 2==0:
#         print(i)

#or

# for i in range(2,21,2):
#     print(i,end=' ')

#task 3 - print odd numbers from 1 to 15
# for i in range(1,16,2):
#     print(i , end=' ')
 #output 1 3 5 7 9 11 13 15 

#task 4 - print each character of the string
# text = "python"
# for char in text:
#     print(char)

#output
# p
# y
# t
# h
# o
# n


#task 5 - print all items in list.

# data = ["data","seience","Ai"]
# for item in data:
#     print(item)

# output
# data
# seience
# Ai

#task 6 - find the sum of numbers from 1 to 10.
# total = 0
# for i in range(1, 11):
#     total += i
# print(total)

#output
#55

#task 7 - print multiplicatiom table of 5.
# for i in range(1,11):
#     print(f"5 x {i} = {5 * 1}")

# output
# 5 x 1 = 5
# 5 x 2 = 5
# 5 x 3 = 5
# 5 x 4 = 5
# 5 x 5 = 5
# 5 x 6 = 5
# 5 x 7 = 5
# 5 x 8 = 5
# 5 x 9 = 5
# 5 x 10 = 50


#task 8 - count how many vowels are in a string
# text = "hello world"
# vowels = "aieouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print(f"Numbers of vowels: {count}")

# output
# Numbers of vowels: 3

#task 9 - print numbers in reverse order from 10 to 1

# for i in range(10,0,-1):
#   print(i)

# output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


#task 10 - print square of numbers from 1 to 5
# for i in range (1,6):
#     print(i ** 2)

# output
# 1
# 4
# 9
# 16
# 25

#task 11 - 
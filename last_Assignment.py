# # last_Assignment.py

# # 1. Basics of Python

# # Write a Python program to print "Hello, World!".

# # x = ("Hello, World")
# # print(x)

# # # Write a program to take user input for their name and print a greeting message.

# # a =(input('Shailesh:')) 
# # D = ("Hello, Shailesh")
# # print(D) 

# # What is the difference between print() and input() in Python?
 
# # x = ("Hello, World")
# # input(x)               #There is nothing diffrence Between pritn()  & input()
 
# # Write a program to swap two variables without using a third variable.


# # a = 3
# # b = 7
# # # a = b 
# # print(a)

# # b = a
# # print(b)

# # # Write a Python script to check the type of a variable

# # x = ("hello")
# # y = 1 

# # print(type(x))
# # print(type(y))


# # Datatype & variables

# # What are mutable and immutable data types in Python?

# # 1. mutable data type :-

# #  - list :
# # x = ["shailesh", "dev"]
# # print(x)

# # #  - Dictionaries 
# # person1 = { 
# # "name": "John", 
# # "age": 36, 
# # "country": "Norway" 
# # } 
# # print(person1)

# #  - set 
 
# # set = {1, 2, 3, 4, 11, 15, 2, 3, 15}
# # print(set)

# # immutable data:-
# # #  Integer - 
# # x = [1,3,2]
# # print(x)

# #  string - 

# #  tuple - 
 
# # Write a program to convert an integer to a string and vice versa.

# # Write a program to check if a number is of integer type.
# # Function to check if a number is an integer
# def is_integer(value):
#     return type(value) == int

# value = 123

# print(is_integer(value)) 

# value = 12.34
# print(is_integer(value))  

      
# # What will be the output of print(type([]) is list)? Explain why.
 
# thislist = ["apple"]
# for x in thislist:
#     print(type[x])

# # Create a dictionary with three key-value pairs and print the value of a specific key


# my_dict = { 
# "name": "John", 
# "age": 36, 
# "country": "Norway" 
# } 
# print(my_dict["age"])


 # 3. Write a Python program to demonstrate the use of all arithmetic operators.


# # Addition (a + b)
# a = 10
# b = 5
# print(a + b)

# # Subtraction (a - b)
# print(a - b)

# # Multiplication
# print(a * b)

 # division
# print(a / b)

 # Modulus 
# print(a % b)

# # What is the difference between is and == operators?

# a = 1
# b = 1 
 #  print( a == b )  ( Compares the memory addresses of the two objects to see if they are the exact same object.)

# a = [1,2,3]
# b = [1,2,3]
# print(a is b ) 


 # == compares values (whether they are the same).
 # is compares identities (whether they are the exact same object in memory).


# # # Write a Python program to check if a number is even or odd using conditional operators.

# num = int(input("Enter a number: "))

# if num %2  == 0:
#     print(num, " is even")
# else:
#     print(num," is odd")


# # # Explain the working of bitwise operators in Python with an example.
# a = 5   
# b = 3   

# # AND Operator
# and_result = a & b
# print(f"{a} & {b} = {and_result}") 

# # OR Operator
# or_result = a | b
# print(f"{a} | {b} = {or_result}")  

# # Write a program to swap two numbers using bitwise XOR.
 
# a =(input('enter the value:'))
# # x = [1, 2, 3, 4]
# swapped_x = a[::-1]
# print(swapped_x)

# Control Flow (if-else, loops)
# Write a program to check if a given number is positive, negative, or zero.

# number = int(input("enter the number - "))

# if number > 0:
#     print("the number is possitive")
# elif number < 0:
#     print("the number is negetive")
# else:
#     print("the number is zero")


# Write a Python program to print the first 10 numbers using a for loop.

# for x in range(1 , 11):
#     if x %2 == 0:
#           print(x, "is even")
#     else:
#          print(x, "is odd") 

# Write a Python program to calculate the factorial of a number using a while loop.

# number = int(input("Enter a number: "))
# x = 1

# while number > 0:
#     x *= number  
#     number -= 1  
# print(x)

# What is the difference between break and continue statements? Give examples.
# # Loop through numbers 1 to 5
# for x in range(1, 6):
#     if x == 3:
#         print("Skipping x = 3")
#     print(x)

# Write a program to check whether a given year is a leap year.

# year = int(input("Enter a year: "))

# if (year % 4 == 0):
#     print(year, "is a leap year.")
# else:
#    print(year, "is not a leap year.")

# Write a function to find the sum of two numbers. 

# x = 5
# y = 10 
# result = int( x + y)
# print(result)
 
# Explain the difference between return and print() in functions.
# return:
# Purpose: return is used to send a result back from a function to the place where it was called. When a function reaches a return statement, it exits the function and optionally passes a value back to the caller.

# 2. print():
# Purpose: print() is used to display output to the console or terminal. It doesn't affect the flow of the program or return any value to the caller. It simply shows the value for the user to see.

 
# Write a recursive function to calculate the factorial of a number.
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(10)
# print(result)  



# What is the use of *args and **kwargs in function definitions?
#  args
# def my_function(*kids):
#     print("The youngest child is " + kids[1]) 
# my_function("Emil", "Tobias", "Linus") 

# kwargs
# def my_function(country = "Norway"):
#     print("I am from " + country) 
# my_function("Sweden") 
# my_function("India") 
# my_function()
# Write a function that takes a list and returns a new list with only even numbers.

# x = int(input("enter the number:"))
# for x in range(1 , 11):
#      if x %2 == 0:
#           print(x, "is even")

# 6. Lists and Tuples
# Write a Python program to find the largest element in a list.
# thislist = [1,2,3,4,5,6]
# print(max(thislist))

# What is the difference between a list and a tuple?
# tuple
# Unchangeable 
# Tuples are unchangeable, meaning that we cannot change, add or remove items 
# after the tuple has been created

# Write a Python program to reverse a list without using reverse().

# thislist = [1,2,3,4,5]
# thislist.sort(reverse= True)
# print(thislist)
# # Write a program to find the sum of all elements in a tuple.
 
# def x(*args):
#     return sum(args)
# result = x(1,2,3,4)
# print(result)


# # Explain how list slicing works in Python with an example

# b = "Hello, World!" 
# print(b[2:5]) 
# b = "Hello, World!" 
# print(b[:5])
# b = "Hello, World!" 
# print(b[2:])

# 7. Strings
# Write a Python program to check if a string is a palindrome.

# def is_palindrome(x):
    
#     x = x.lower()
    
# word = input("Enter a word: ")
# if is_palindrome(word):
#     print(f'"{word}" is a palindrome!')
# else:
#     print(f'"{word}" is NOT a palindrome.')

# What is the difference between split() and join() methods?

# Split
# x = "apple banana cherry"
# words = x.split()
# print(words)

# Join
# words = ['apple', 'banana', 'cherry']
# text = " ".join(words)  
# print(text)


# # Write a program to count the number of vowels in a given string.
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
    
#     for char in s:
#         if char in vowels: 
#             count += 1
    
#     return count
# text = input("Enter a string: ")
# print(f"Number of vowels: (count_vowels(text)0")



# Write a Python program to replace all occurrences of a word in a string.
# 
# a = "Hello, World!"
# print(a.replace("H", "Hi H")) 



# Web Scraping
# import requests # type: ignore
# from bs4 import BeautifulSoup # type: ignore

# def scrape_titles(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     titles = soup.find_all('h1')
#     for title in titles:
#         print(title.text)

# url = input("Enter the URL to scrape: ")
# scrape_titles(url)


# in python a function is some reusable code that takes arguments as input, does some computation , and then return a result or results
# .we define a function using the def reserved word 
# . we call/ invoke the function by using the function name,
# parenthesis, and arguments in an expression

# There are two types of function:
# [1] built in function  like int(),float(),print()
# [2] self made function like calling a function.
# a non local keyword is a word when we want to declare a vriable 
# in the local scope but act as global scope
# a global keyword is keyword to replace local variables inside function
# a variable which comes under function is called local variable 
# a variable which mention outside of function is called global variables
# in function there are four types of arguments allowed.
# positional Arguments(argument passed as parameter)
# keyword Arguments
# default Arguments
# variable-length arguments(we mention variable with*symbol and passed as many argument as we want)
# lambda function are one liner function without any names,it is a nameless property function
# is also called anonymous function:
# lambda() takes iterables as a first argument followed by key parameter which takes function as an argument to be applied to iterables parameter 
# followed by reverse which takes True and False argument .
# filtere()function is used based on condition with lambda function.
# it is used to return the filtered value.
# map function is used with lambda for modifying date of iterables like list:
# it is used in dictionary to set key and values 
# and it apply given function to all items in an iterable.
# in order to iterate over multiple iterable(list) use map function:

# x = 99
# # def function1():
# #     print("value is ",global_var)

# def function2():
#     global x
#     x = 56
#     print("value is ",x)
# function2()
# # function1()
# # function2()

# sum of two numbers.Using local variables to store no. and result.
# def add():
#     a = 5
#     b = 6
#     addy = a + b
#     print(addy)
# add()

# using global variable as local variable
# x = 5
# c = 7
# def calc():
#     global x
#     global c
#     x = 4
#     c = 6
# addy = x + c
# print(addy)
# calc()

# creating a global variable and accessig it inside a function:
# global_variable = 'hello im  a programmer'
# def string():
#     global global_variable
#     global_variable = 'hello im a python programmer'
# print(global_variable)
# string()
# modifying global variables in local variables:
# x = 5
# def cou():
#     global x
#     x = x + 6
#     print(x)
# cou()

# def ca():
#     y = x + 3
#     print(y)
# ca()

# # accessing global and local outside the function:
# l = 'hello im a  programmer'
# def al():
#     print(l)
# print(l)
# al()

# modifying global variables:
# global_1 = 4
# def add():
#     global global_1
#     global_1 += 4
#     print(global_1)
# add()

# def outer_fuc():
#     outer_fuc = 'im an outer variable'
    
#     def inner_fun():
#         nonlocal outer_fuc
#         outer_fuc = 'im an developer'
#         print(outer_fuc)
#     inner_fun()
#     print(inner_fun)
# outer_fuc()

# def outer_function():
#     outer_var = "I am an outer variable"

#     def inner_function():
#         nonlocal outer_var
#         outer_var = "I am modified by inner function"
#         print("Inside inner function:", outer_var)

#     inner_function()
#     print("Inside outer function:", outer_var)
# outer_function()

# keyword arguments in function:
# def message(name,surname):
#     print("hello",name,surname)
# message(name = 'rei',surname = 'peter')

# keyword arguments:
# def message(name,surname):
#     print(surname,name,'is a programmer')
    
# # message(name = 'jony',surname = 'rakhe')
# message(surname = 'rei',name = 'peter')

# example of default arguments:
# def message(name = 'peter'):
#     print('hello',name)
# message('hello im a programmer')

# variable length arguments:let us passs multipl arguments all at once:
# def wish(*name):
#     print(name,'congrats for staying true to your word,life is too small to regret too big to explre')
# wish('peter','john','karry')

# fibonacci sequence in recursive function:
# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(9))

# lambda function to iterate over tuple sequence:
# l = 'potato','tomato','chilli','red'
# k = tuple(filter(lambda x:x ,l))
# print(k)

# lambda function to print even  numbers:
# l = [1,33,2,3,4,5,3,33,22,667,12456]
# k = list(filter(lambda x:x % 2 == 0 ,l))
# print("even numbers are ",k)

# # simple greet function:
# def greet(name):
#     print(f"hey {name} how are you its been long time")
# greet('spiderman')
# # # return sum using simple function definition:
# # def add(a,b):
#     add = a + b
#     return add
# print(add(4,5))

# default function argument:
# def show_employee(name,salary = 9000):
#     print(f"emplyee {name} and salary {salary}")
# show_employee("john")
# show_employee("parker")

# # variable length argument function:
# def print_values(*name):
#     print(f"hey {name} its been long time since we all met",)
# print_values('parker','john','karry','mony','jarry')

# # example of keyword arguments:
# def describe_persons(name,age,city = 'kolkata'):
#     return f"hello im {name} and im currently  {age} and i live in {city}"
# print(describe_persons('peter',54,'japan'))

# # example of variable length arguments:
# def find_max(*l):
#     if not l:
#         return 0
#     return max(l)
# print(find_max(23,33,22,11,2124))

# nested function to return the result of inner to outer function:
# def outer(n):
#     def inner(x):
#         return x + 4
#     return inner(n)
# print(outer(6))

# recursive function to calculate nth fibonacci numbers:
# def recur_fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1 
#     return recur_fibo(n-1) + recur_fibo(n-2)
# print(recur_fibo(10))
# product of two argumenst using map function:
# l1 = [12,2,3,4]
# l2 = [23,3,4,5]
# result = list(map(lambda x,y:x*y,l1,l2))
# print(result)

# merging two list using reduce in lambda function:
# from functools import reduce
# l1 = [12,2,3,4]
# l2 = [2,3,4,56]
# combined_list = l1 + l2
# result = reduce(lambda x,y: str(x)+str(y),combined_list,' ')
# print(result,)

# concatenating two list using lambda function:
# l1 = ['hello','hi','good']
# l2 = ['world','there','morning']
# result = list(map(lambda x,y: (x+" "+y),l1,l2))
# print(result)

# x = 50
# def globe():
#     # global x
#     x = x + 1
#     print(x)
# globe()
# print(x)

# checking for palindrome:
# def reverse_l(lst):
#     for k in lst:
#         if k == k[::-1]:
#             print(k)
# lst = ['mam','dog','lool','racecar']
# reverse_l(lst)

# CALENDAR CONSTANT,MODULE USING FUNCTION :
# import calendar 
# def is_weekend(day):
#     return day in (calendar.SATURDAY,calendar.SUNDAY)
# day_mapping = {1:calendar.MONDAY,  
#             2:calendar.TUESDAY, 
#             3:calendar.WEDNESDAY,
#             4:calendar.THURSDAY,
#             5:calendar.FRIDAY,
#             6:calendar.SATURDAY,
#             7:calendar.SUNDAY}
# day_input = int(input("enter day number "))
# day = day_mapping.get(day_input)

# if is_weekend(day):
#     print("its the weekend! ")
# else:
#     print("its a weekday ")

# nums = [12,2,3,4,2,3,5]
# e = [x ** 2 for x in nums]
# print(e)

# nums = [23,3,4,2,4]
# e = [x for x in nums if x % 2 == 0]
# print(list(e))

# animals = ['lion','tiger','monkey','elephant','frog']
# filtered_animals = [animal for animal in animals[:animals.index('elephant')]]
# print(filtered_animal)


# importing libraries
# a = 9
# def swap(a,pos1,pos2):
#     bit1 = (a>> pos1) & 1 
#     bit2 = (a>> pos2) & 1
    
#     if bit1 != bit2:
#         a ^= (1 << pos1) | (1 << pos2)
#         return a
# a = 28
# pos1 = 1
# pos2 = 3
# print(swap(a,pos1,pos2)
# su = 0
# for i in range(101):
#     su += i
# print(s
# import sys
# while True:
#     user = int(input("enter num"))
#     if user == 1:
#         print("hello")
#     elif user == 2:
#         print("howday")
#     else:
#         print("greeting")
#         sys.exit()

# x = 10
# def greet():
#     global x
#     x = 20
# greet()
# print(x)
        
# lexicograph of characters:  
# big = ('hello world')
# for char in big:
#     print(ord(char))
    

# sval = '124 c5ar'
# k = (sval.split(''))
# print(k)

# def compute_pay(hour,rate):
#     try:
#         hour = float(hour)
#         rate = float(rate)
#         pay = hour * rate
#     except ValueError:
#         print('enter numeric value not string ')
        
#     else:
#         if hour > 40:
#             pay = 40 * rate + (hour - 40) * 15
#         print('worked ',hour,'hours')
#         print(rate,'amount per hour')
#         print('ur total working amount pay is ',pay)
# hour = input('enter hours u worked:')
# rate = input('enter rate per hour:')
# compute_pay(hour,rate)


# def format_name(first_name,last_name):
#     return f'{first_name.title()},{last_name.title()}'
    
# print(format_name('rei nanung','programmer'))


# from functools import lru_cache
# @lru_cache
# def fib(n):
#     if n == 0 or n == 1:
#         return n 
#     else: 
#         return fib(n-1) + fib(n-2) 

# for i in range(1,11):
#     print(f'{i}: {fib(i)}')

# tasks = []

# def add(task):
#     tasks.append(task) 
#     return tasks

# def view_task():
#     return tasks

# def delete_task(user):
#     if user in tasks:
#         tasks.remove(user)
#         print(f'task {user} removed ')
#     else:
#         print(f'task {user} dont exist ')
            
# def main():
#     while True:
#         user_input = input("Enter 'add' to add: 'view to view_task 'delete' to delete: 'exit' to quit:")
#         if user_input == 'add':
#             task = input('Enter today\'s task:')
#             print(add(task))
        
#         elif user_input == 'view':
#             print(view_task())
        
#         elif user_input == 'delete':
#             user = input('delete task:') 
#             delete_task(user)
            
#         else:
#             print('Invalid input enter valid tasks :')
#             break
            
# main()
        
        
# def main():
#     task = input('enter your task:') 
#     print(add(task))
# main()










# def view_task():
#   return tasks

# def delete_task(task):
#     if task in tasks:
#         tasks.remove(task) 
#         return (f'task {task} removed..')
#     else:
#         return(f'task{task} doesnot exists') 

# def main():
#     while True:
#         print('\n Today\'s task :', view_task())
#         user_input = input("enter to 'add' task \n'delete' task\n'exit' to quit:").strip().lower()
        
#         if user_input == 'add':
#             user_task = input('enter your daily task:').strip() 
#             add(user_task) 
#             print(f'task added {user_task}') 
        
#         elif user_input == 'delete':
#             user_input = input('enter task to delete:') 
#             print(delete_task(user_task))
        
#         elif user_input == 'exit':
#             break 
        
#         else:
#             print('Invalid input.Please try again:')
# main()


# tasks = []
# def add(task):
#     tasks.append(task)
#     return tasks 
# task = input('enter your task:')
# print(task)

# def delete_task(user):
#     global tasks
#     if user in tasks:
#         tasks.remove(user)
#     else:
#         print(tasks) 
# user = input('enter task to delete:') 
# delete_task(user)
  
# tasks = []

# def add(task):
#     tasks.append(task)
#     return tasks 

# # Add a task
# task = input('Enter your task: ')
# add(task)
# print(f'Task added: {task}')

# def delete_task(user):
#     if user in tasks:
#         tasks.remove(user)
#         print(f'Task "{user}" removed.')
#     else:
#         print('Task does not exist.')

# # Get user input for deletion
# user = input('Enter task to delete: ')
# delete_task(user)

# # Print the updated list of tasks
# print('Updated tasks:', tasks)
# from functools import lru_cache
# from functools import lru_cache
# import time
# t = time.time() 
# @lru_cache
# def increment(num):
#     print('running 1000 line of code') 
#     return num + 1

# print(increment(1))
# print(increment(2))
# print(increment(3))
# print(increment(4))
# print(increment(3))
# e = time.time()
# print(f'{e-t:.2f}')

# def my_decorator(func):
#     def wrapper():
#         print("hello progammer")
#         func()
#         print('im new to programming') 
#     return wrapper

# @my_decorator
# def say_hello():
#     print('hi to all newbies') 
# say_hello()

# import time 
# t = time.time()
# li = ['add','subtract','multiplication','division','remainder']
# def add(x,y):
#     return x + y 

# def subtract(x,y):
#     return x - y

# def multiplication(x,y):
#     return x * y 

# def division(x,y):
#     return x  / y 

# def remainder(x , y):
#     return x % y 

# while True:
#     def main():
#         user = input('choose from the following operation to performm: add ,multiplication, subtraction,  division, remainder:')
   
#         if user == 'add':
#             x = int(input('enter the number:')).strip()
#             y = int(input('enter the number:'))
#             print(add(x,y))
            
#         elif user == 'subtraction':
#             x = int(input('enter the number:'))
#             y = int(input('enter the number :'))
#             print(subtract(x,y))
            
#         elif user == 'multiplication':
#             x = int(input('enter number:'))
#             y = int(input('enter number:')) 
#             print(multiplication(x,y))
        
#         elif user == 'division':
#             x = int(input('enter number:')) 
#             y = int(input('enter number:'))
#             print(division(x,y))
            
#         elif user == 'remainder':
#             x = int(input('enter number:'))
#             y = int(input('enter number:')) 
#             print(remainder(x,y))
        
#         else:
#             print('Enter valid operation:')
#     break
# main()
# e = time.time()
# print(f'{e-t:.2f} seconds')
# fibo = [0,1]
# for i in range(1,11):

# def fibo(n):
#     a , b = 0,1
#     for _ in range(n):
#         a , b = b , a + b 
#     return a
# print(fibo(10))

# from functools import reduce
# def add(x,y):
    
#     return x + y 
# nums = [23,4,5,3,5,6] 
# k = reduce(lambda x , y: x + y ,nums)
# print(k)

# from functools import reduce 
# k = [23,4,5,11,55,67] 
# c = reduce(lambda x , y : y if y < x else x , k )
# print(c)

# text = input('enter string: ')
# ascii_values = [ord(char) for char in text] 
# binary_values = [format(value,'08b') for value in ascii_values] 
# binary_string = ' '.join(binary_values) 
# print(binary_string)

# t = ['t','g','e','g','f','a']
# a = []

# for char in t:
#     ascii_values = ord(char)   
#     a.append(ascii_values) 
# n = map(lambda item : bin(item)[2:].zfill(8),a)
# binary = ' '.join(n)
# print(n)

# import math 
# def is_prime(n):
#     if n <= 1:
#         return False 
#     for i in range(2,int(math.sqrt(n))+ 1):
#         if n % i == 0:
#             return False 
#     return True

# def print_primes(n):
#     for num in range(2,n + 1):
#         if is_prime(num):
#             print(num,end = ' ') 
# n = 78
# print_primes(n)

# def sieve_erathosthenes(n):
#     prime = [True] * (n + 1)
#     p = 2 
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * p, n + 1,p):
#                 prime[i] = False 
#         p += 1 
#     prime_numbers = [p for p in range(2,n + 1) if prime[p]] 
#     return prime_numbers 

# def sum_of_primes(n):
#     prime_numbers = sieve_erathosthenes(n)
#     return sum(prime_numbers) 
# print(sum_of_primes(50))


# from functools import reduce
# s = ['hello','world']
# upperss = []
# for item in s:
#     item = item.upper() 
#     upperss.append(item) 
# print(upperss)

# s = ['we are programmer']
# k = list(map(lambda x : x.upper(),s))
# print(k)

# def convert(user):
#     return ''.join(str(bin(user)))
# user = input('enter a string:') 
# print(convert(user))

# import threading

# def print_numbers():
#     for i in range(1, 6):
#         print(i)

# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)

# # Create threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start threads
# thread1.start()
# thread2.start()

# # Wait for threads to complete
# thread1.join()
# thread2.join()

# print("Done!")
text = 'programming'
print('gram'in text)
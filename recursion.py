# recursion is the process of repeating item in a self similar way.
# algorithimically it is a way to design solutions to problems by divide
# and conquer or decrease and conquer reduce a problem to simpler verisos of the 
# same problem /
# semantically; a progamming technique where a function calls itself.
# in programming goal is not to have infinite recursion.
# must have one or more base cases that are easy to solve
# must solve the same problem on some other input with the goa of simplifying
# the larger problem input
# def recur_fibo(n):
#     fib= [0,1]
#     i = 2
#     while n > i:
#         if n ==i:
#             return n
#         else:
#             return fib(n-1) + fib(n-2)
# n = int(input("enter an integer"))
# print(recur_fibo(n))


# def factorial(n):
#     prod = 1
#     for i in range(1,n+1):
#         prod *= i
#     return prod
# print(factorial(6))

# def factirial(n):
#     if n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial( 6))

# def fibo(x):
#     if x == 0 or x == 1:
#         return 1
#     return fibo(x-1) + fibo(x-2)
# print(fibo(6))

# import time 
# t = time.time() 
# def tower_of_hanoi(n,source,target,auxiliary):
#     if n == 1:
#         print(f'move disk 1 from {source} to {target}') 
#         return n 
#     tower_of_hanoi(n-1 ,source,auxiliary,target) 
#     print(f'move disk {n} from {source} to {target}') 
#     tower_of_hanoi(n-1 , auxiliary,target,source)

# tower_of_hanoi(3,'a','b','c ')
# e = time.time() 
# print(f'{e-t:.2f}sec')

# def fact(n):
#     if n == 0:
#         return 1 
#     return n*fact(n-1)
# print(fact(5))

# def printMove(fr,to):
#     print('move from ' + str(fr) + 'to' + str(to)) 
    
# def Towers(n,fr,to,spare):
#     if n == 1:
#         printMove(fr,to) 
#     else:
#         Towers(n-1,fr,spare,to) 
#         Towers(1,fr,to,spare) 
#         Towers(n-1,spare,to,fr)
# Towers(3,'a','b','c') 

# decorators are a powerful feature in python that allow you to modify the behaviour of functions or method.They are 
# often used for logging,access control ,instrumentation and more.
# a decorator is a function that takes another function as an argument and extends or alters
# its behaviour. decorators are often used to add wrapping functionality to existing functions in a class and readable
# way










# def my_decorator(func):
#     def wrapper():
#         print('something is happening before the function is called') 
#         func() 
#         print('something is happening after the function is called') 
#     return wrapper

# @my_decorator 
# def say_hi():
#     print('hello we are programmer')
# say_hi()

# def compose(f,g,x):
#     return f(g(x))
# compose(print,len,'hello,world!')

# import random 
# def random_power():
#     def f(x):
#         return x**2 
#     def g(x):
#         return x**3 
#     def h(x):
#         return x**4
    
#     function = [f,g,h]
#     return random.choice(function) 
 
# for i in range(5):
#     p = random_power()
#     print(p(3))

# import time 

# def timer(f):
#     def wrapper(*args,**kwargs):
#         s = time.time() 
#         result = f(*args,**kwargs) 
#         e = time.time() 
#         dt = e - s 
#         print(f'{dt}')
#         return result
#     return wrapper


# @timer
# def prime_factor(n):
#     factor = [] 
#     divisor = 2 
    
#     while n > 1:
#         while n % divisor == 0:
#             factor.append(divisor)
#             n //= divisor 
#         divisor += 1
#     return factor

# prime_factorization_timer = timer(prime_factor)
# result = prime_factorization_timer(45)
# print(result) 




# def log(func):
#     def wrapper(*args,**kwargs):
#         print(f'calling function {func.__name__}') 
#         result = func(*args,**kwargs) 
#         print(f'function {func.__name__} finished') 
#         return result 
#     return wrapper

# @log 
# def add(a,b) :
#     return a + b 
# print(add(4,5))

# import time 
# def timer(func):
#     def wrapper(*args,**kwargs):
#         s = time.time() 
#         result = func(*args,**kwargs) 
#         e = time.time() 
#         dt = e-s
#         print(f'function {func.__name__} took {dt:.4f}') 
#         return result 
#     return wrapper

# @timer 
# def slow_function():
#     time.sleep(2) 
#     print('function finished') 
# slow_function()

# def require(func):
#     def wrapper(user,*args,**kwargs):
#         if user != 'admin':
#             print('access denied') 
#             return 
#         return func(*args,**kwargs) 
#     return wrapper 

# @require 
# def delete():
#     print('database deleted') 
# delete('admin') 
# delete('hi')


# import time 
# def timer_decorator(func):
#     def wrapper(*args,**kwargs):
#         s = time.time() 
#         result = func(*args,**kwargs) 
#         e = time.time() 
#         print(f'function{func.__name__} took {e - s:.2f} seconds') 
#         return result 
#     return wrapper 

# @timer_decorator 
# def func(a,b,c = 1):
#     time.sleep(1) 
#     return a + b + c  
# print(func(2,3,c= 5))

# class counter:
#     def __init__(self,x):
#         self._c = x 
#         self.__cc = 10 
        
# c1 = counter(7) 
# print(c1.__counter__cc)


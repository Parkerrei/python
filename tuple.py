
# Tuple are ordered,immutable,and allow 
# duplicate however if an element contains 
# mutable elemennt like list inside tuple then We can mutate
# tuple is an efficient and simpler version of list
# tuple unpacking allows you to assign values from a tuple (or any iterable) to multiple variables in a single statement.
# key requirement is that values and variables must correspond to each other .
# user = input("enter ur three favourite movies : ")
# list = []
# user1 = list.append(user)
# print(list)


# list = ['racecar','bottom','mom']
# list2 = list.deepcopy() 
# list = list2.append('tom')
# list3 = list2.count('bottom')
# print("it\'s a copied list",list2)
# print(list3)
# print(list)
# reverse_list = list.reverse() 
# for item in list:
#     if list == reverse_list:
#         print("its palindrome")
#     else:
#         print("not palindrome")

# list = input("enter a value : ")

# reverse = list[::-1]

# if list == reverse:
#     print("its palindrome")
# else:
#     print("not palindrome")
    
#  using copy() to search for palindrome:
# list = ["mam","noon",",mam",121]
# list2 = list.copy()
# reverse = list2.reverse
# if list == list2:
#     print("it's palindrome")
# else: 
#     print("its not palindrome")
    
    
# list = ['3,2,3,3,2,5']
# ls = '3'
# count = 0
# for item in list: 
#     count += item.count(ls)
# print(count)

# tup = ('C','D','A','A','B','B','A')
# list1 = tup.count("A")
# # list2 = tup.sort()
# print(list1)
# print(tup)


# updating movies in a empty list:
# movies = []
# while True:
#     user1 = input('enter movies name: ')
#     if user1 == 'q':
#         break
#     else:
#         movies.append(user1)
# print(movies)


# with open('.txt','r',encoding = 'utf-8') as files:
#     data = files.read() 
# if data.isspace():
#     print('its in space')
# else:
#     print('no white space')

# from random import randint
# n = []
# while True:
#     random = randint(0,10)
#     if random == 0:
#         break 
#     else:
#         n.append(random)
# print(n)

# import timeit 
# list1 = timeit.timeit(stmt = '[3,4,5,6]') 
# print(list1,timeit)

# def find(list1):
#     return  f'maximum value is :{max(list1)},\nminimum value is :{min(list1)},\naverage is :{sum(list1)//len(list1)}'
# list1 = [3,45,5,67,78,4] 
# print(find(list1))

# def fibo(n):
#     a,b = 0,1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     for _ in range(2,n+ 1):
#         a,b = b, a+ b 
#     return b 
# n = 10
# print(fibo(n))

def data(dict):
    keys = list(dict.keys()) 
    values = list(dict.values())
    return f'keys are : {keys},\nvalues are : {values}'
dict = {'name':'peter','work':'programmer','age':34}
print(data(dict)) 
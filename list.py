# '''list is an built in data type and stores stores
#  values of different order or types. 
# for ex:integer,float,boolean'''
# list is an ordered mutable collection of item
# list are slower than tuples because of their mutability
# list consumes more memory because they need to store additional data 
# use list when u need to collect different kind of data structures that need to be changed
# list are order sequence of data.


# LIST METHOD OR BUILT FUNCTION: 
# [1] append() adds an element to end of list:
# [2] extend() adds all element of an iterable(like another list)
# to end of the list. 
# [3] insert() insert an element at a specified position. 
# [4] remove() remove first occurence of an Element
# [5] pop() pops out the last element unless u specified with index. 
# [6] clear() removes all data
# [7] index() returns the index of an element unless specified.
# [8] count() returns the no. of ocurence of an element unless specified     
# [9] sort() returns the sorted version of list in ascendng and descending order    
# [10] reverse() returns the altered versions of list  
# [11] copy() returns the copy of original list
# [12] deepcopy() returns the original list but with a new list.
# [12] list() returns empty list and can also converts any data types to a list
# [13]isinstance() takes index value and element as arguments and returns us unique literals.
# [14]random.choice() and random.shuffle and rand.randint() methods of list:
# [15] sorted() returns a new sorted list without changing the original list unlike sort() which changes the original list:
# sorted() is used to sort all iterables(tuples,set,list,strings) unlike sort() which is only confined to list 

# concatenating two list index wise:
# list1 = ['m','na','i','ke']
# list2 = ['y','me','s','lly']
# list3 = len(list1+list2)
# list4 = []
# for i in range(list3):
#     list4 = list1[0] + list2[0],list1[1] +list2[1],list1[2]+list2[2],list1[3]+list2[3]
# print(list4)

# squared list of numbers
# n = [12,2,3,4,2]
# sq = []
# for num in n:
#     num = num**2
#     sq.append(num)
# print(sq)

# CONCATENATING TWO LIST IN ClOSE ORDER:
# list1 = ['hello','take']
# list2 = ['dear','sir']
# list3 = list1[0] + list2[0],list1[0]+list2[1],list1[1]+list2[0],list1[1]+list2[1]
# print(list(list3))
# print(list4,sep=',')
# print(list3,sep=',')

# list1 = [10,20,30,40]
# list2 = [100,200,300,400]
# list3 = list2[::-1]
# for item1,item2 in zip(list1,list3):
#     print(item1,item2,end=',')

# l = [1,2,3]
# r = ['a','b','c']
# g = list(zip(l,r))
# h = l+ r
# print(h)
# print(g)

# REMOVE EMPTY STRING FROM A LIST:
# list1 = ['mike','','ema','kelly','','brad']
# for item in list1:
#     if item == '':
#         list1.remove(item)
# print(list1)

# interchanging first and last element
# list1 = [10,33,4,5]
# list1[0],list1[-1] = list1[-1],list1[0]
# print(list1)

# ways to find lenth of list:
# def recur(l):
#     if len(l) == 0:
#         return l
#     return len(l) 
# l = [12,2,3,5,4,31,1]
# print(recur(l))
        
# l = ['st','d']
# k = ['d','d']
# if l>k:
#     print(True)
# elif k>l:
#     print("ok")
# else:
#     print(False)
# print(type(l))
# print(list())
# a = [12,3,67]
# b = a.insert(1,22)
# c = list()
# print(c)
# b = a.copy()
# print(a)
# print(k)
# l = [12,22,1,2,4,2]
# l[2] = 45
# print(l)
# k = l[::-1]
# print(k)

# catnames = []
# while True:
#     print('enter the name of cat' + str(len(catnames) + 1)+ '(or enter nothing to stop.):')
#     name =  input()
#     if name == '':
#         break 
#     catnames += [name]
#     print("the cat names are : ")
#     for name in catnames:
#         print( name, end = '\n')

# spam = []
# while True:
#     print('enter catnames : ' + str(len(spam) + 1))
#     name = input()
#     if name == '':
#         break
#     spam += [name]
# print("cats name are")
# for name in spam:
#     print('',name)

# # multiple assignment trick(tuple unpacking):assinging each element a variable in a list:
# l = ['pen','oot','sopi','owl']
# black,name,cat,bird = l
# k = f'this is a black {black} and my name is {name} and this is \n sister {cat} and meet my bird {bird}'
# print(k)       

# enumerate function to gain access element and index at same time:
# lst = ['pen','to','owl','oos']
# for index,item in enumerate(lst):
#     print(f'index {index}, item {item}')

# RANDOM EXERCISE:
# import random 
# pets = ['dor','cat','moose']
# k = random.choice(pets)
# print(k)

# pets = ['dor','cat','moose']
# k = pets[random.randint(0,len(pets)-1)]
# print(k)

# random.shuffle function to alter the list:
# import random
# people = ['alice','bob','carol','david']
# k = random.shuffle(people)
# print(people)
    
# ast = abstract syntax trees:
# import ast 
# while True:
#     try:
#         k = input("enter value separated by commas: ")
#         s = ast.literal_eval(f'[{k}]')
#         s.sort()
#     except (ValueError,SyntaxError,TypeError,AttributeError):
        
#         print('enter valid value : ')
#     else:
#         print('sorted list',s)
#         break
    
# import random

# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])

# import copy
# spam = ['a','b','c','d','e']
# k = copy.copy(spam)
# k[2] = 'mango'
# print(spam)

# d = copy.deepcopy(spam)
# d[2] = 'apple'
# print(spam)

# import copy

# original_list = [[1, 2, 3],[4, 5, 6]]

# # Shallow copy
# k = copy.copy(original_list)
# k [0][0] = 8
# print("Original list after shallow copy modification:", original_list)

# # Deep copy
# # d = copy.deepcopy(original_list)
# # d [0][0] = 9
# # print("Original list after deep copy modification:",original_list)

# def s(items):
#     if not items:
#         return ''
#     elif len(items) == 1:
#         return str(items[0])
#     else:
#         return ','.join(map(str,items[:-1]))+ ', and ' + str(items[-1])
# items = ['apple','mango','grapes','peter']
# print(s(items))

# converting list into single list of string:
# def lst(li):
#     if not li:
#         return ''
#     elif len(li) == 1:
#         return str(li[0])
#     else:
#         return ','.join(map(str,li[:-1])) + ', and ' + str(li[-1])
    
# li = ['apple','mango','banana','tofu']
# print(lst(li))

# from functools import reduce
# from operator import concat

# country = [['india','nepal','japan'],
#           ['china','tokyo','bangla'],
#           ['myanmar','us','srilanka']]

# for i in range(len(country[0])):
#     for x in range(len(country)):
#         print(country[x][i])

# rows = int(input("enter no.of rows: "))
# columns = int(input("enter no.of columns: "))
# symbol = input("enter symbol to use: ")
# for x in range(rows):
#     for i in range(columns):
#         print(symbol,end = ' ')
#     print()

# list1 = [1,2,3]
# list2 = [4,5,6]
# i = 0

# while i < len(list1):
#     j = 0
#     while j < len(list2):
#         print(list1[i], list2[j])
#         j += 1
#     print()
#     i += 1
# try:
#     for i in list1:
#         for k in list2:
#             print(list1[i],list2[k])
#         print()
# except IndexError:
#     print("enter valid value")


# for i in range(10):
#     for x in range(i):
#         print('-',end = ' ')
#     print()
    
# for x in range(10,1 ,-1):
#     for p in range(x):
#         print('-',end = ' ')
#     print()

# for x in range(10):
#     for a in range(1,(10 - x)+1):
#         print(' ',end = ' ')
#     for symbol in range(1,x+1):
#         print('-',end = ' ')
#     print()

# total_row = 10
# for e in range(10,0,-1):
#     for a in range(1,(total_row - e)+ 1):
#         print(' ',end = ' ')
#     for symbol in range(1,e + 1):
#         print('-',end = ' ')
#     print()


# total = 0
# count = 0
# average = 0
# while True:
#     user = input('enter a number :')
#     if user == 'done':
#         break
#     try:
#         user = int(user)
            
#     except ValueError:
#         print('enter number not string:')
#         continue
    
#     count += 1
#     total += user
#     average = total//count
# print('vola u are a progammer now ')
# print('count of user are :',count)
# print('total of user are:',total)
# print('average of user are:',average)


# blocks = [] 
# while True:
#     block = f.read(32) 
#     if block == '':
#         break 
#     blocks.append(block) 
# blocks = [] 
# for block in iter(partial(f.read,32),''):
#     blocks.append(block)

# def find(seq,target):
#     found = False 
#     for i , value in enumerate(seq):
#         if value == target:
#             found = True 
#             break 
#     if not found:
#         return -1 
#     return i
# seq = [2,3,4,1]
# target = 0
# print(find(seq,target))

# # Sorting a list of numbers
# numbers = [3, 1, 4, 1, 5, 9]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # Output: [1, 1, 3, 4, 5, 9]

# # Sorting a list of strings
# words = ["banana", "apple", "cherry"]
# sorted_words = sorted(words)
# print(sorted_words)  # Output: ['apple', 'banana', 'cherry']

# # Sorting with a custom key
# people = [{"name": "John", "age": 25}, {"name": "aane", "age": 30}, {"name": "dave", "age": 20}]
# sorted_people = sorted(people)
# print(sorted_people)  # Output: [{'name': 'Dave', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]

# # Sorting in reverse order
# sorted_numbers_desc = sorted(numbers, reverse=True)
# print(sorted_numbers_desc)  # Output: [9, 5, 4, 3, 1, 1]
# li = [3,3,5,7,8]
# k = list(map(lambda x : x ** 2, li ))
# # print(k)

# from functools import lru_cache

# @lru_cache 
# def count_vowels(sentence):
#     return sum(sentence.count(vowel) for vowel in 'aeiouAEIOU') 
# print(count_vowels('hello world')) 

# def listsum(numbers):
#     if not numbers: 
#         return 0 
#     else: 
#         (f,rest) = numbers 
#         return f + listsum(rest) 
# numbers = (1,(2,(3,None))) 
# total = listsum(numbers) 
# print(total)

# strings = ['apple','','mango'] 
# k = [s for s in strings if s == ''] 
# print(k)

# strings = ['apple','','mango'] 
# k = any(s for s in strings if s == '')
# print(k)
 
def recur_function(n): 
    if n == 0 or n == 1: 
        return(1) 
    else: 
        return recur_function(n-1)
print(recur_function(4))
 



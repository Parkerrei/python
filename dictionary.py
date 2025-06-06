# Dictionary are use to store datea values /n in key:value pairs.
# They  are unordered , mutable but dont allow
# duplicate keys
# setdefault method to add new key value pairs to dictionary or check for existing keys .
# items()methods prints out all the key and values in tuple format.
# get()methods takes key as its argument and provides value.u can pass default values along with 
# argument if key is not found in dictionary data structure.
# keys() methods prints out all key from dictionary data structure in tuple list format.
# values() methods prints out all values in tuple and list format.
# in dictionary python read from left to right and when it encounters duplicate key it replace 
# the first key with the last key.
# dictionary are fundamental tool for linking counting and grouping .
# clear() remove all elements from the dictionary 
# copy() returns a copy of the dictionary 
# pop() remove the elements with specified key 
# popitems() removes the last inserted key-value pair 
# update() updates dictionary with specified key=value pairs 

#  for example:
# info = {'key':'value',
#         'name':'parker',
#         'grade':'A'}
# fo = info.update({"city":"haryana"})
# print(info)
# dad = list(info.items())
# d = type(dad)
# print(d)
# print(dad)

# assign values to empty dictionaries:

# dict1 = {}
# dict1[34] = 'age'
# print(dict1)

# dicti = {}
# dicti['table'] = 'a piece of furiniture,list of facts and figures'
# dicti['cat'] = 'a small animal'
# print(dicti)
# print(type(dicti))

# subject = 'python','java','c++','python','javascript','python','java'

# classroom =  len(subject)
# print(classroom,'classrooms are needed for all students')

# dicti = {}
# x = int(input("enter a maths marks : "))
# x = int(input("enter a biology marks : "))
# x = int(input("enter a science mark : "))
# d = dicti.update({'maths':x})
# e = dicti.update({"bilogy":x})
# f = dicti.update({"science":x})
# print(dicti)

# students = {'ajay':89,'jay':91,'shantanu':88,'vicky':91}
# for student in students.items():
#     print(list(student))

# spam = {'colour':'black','name':'peter'}
# k = spam.setdefault('name','prorammer')
# print(spam)
# print(spam.get('class','enter valid key'))

# message = 'It was a bright cold day in april ,and the clocks were striking thirteen.'
# count = {}
# for char in message:
#     count.setdefault(char,0)
#     count[char] = count[char]+ 1
# print(count, end = '')
# print()

# mes = 'hello'
# count = {}
# for char in mes:
#     count.setdefault(char,0)
#     count[char] = count[char] + 1
# print(count)
    
# turn = 'x'
# for i in range(9):
#     printboard(the_board)
#     print("turn for " + turn + '.move on whch space?')
#     move = input()
#     the_board[move] = turn 
#     if turn == 'x':
#         turn = 'o'
#     else:
#         turn = 'x'
# printboard(the_board)

# all_guest = {'alice': {'apple': 5, 'pretzels': 12},
#              'bob'   :    {'ham_burger': 3, 'apple': 1},
#              'carol' :  {'cups': 3, 'apple_pies': 6}}

# def totalbrought(guests,item):
#     num_brought = 0
#     for k , v  in guests.items():
#         num_brought += v.get(item,0)
#     return num_brought

# print('number of thing being brought:')
# print(' - apple          ' + str(totalbrought(all_guest, 'apple')))
# print(' - cups           ' + str(totalbrought(all_guest, 'cups')))
# print(' - cakes          ' + str(totalbrought(all_guest, 'cakes')))
# print(' - ham_burger     ' + str(totalbrought(all_guest, 'ham_burger')))
# print(' - apple_pies     ' + str(totalbrought(all_guest, 'apple_pies')))

# counting number of occurence of words in text file and storing in dictionary data structure:

# import pprint
# with open('webbrowser.txt','r') as files:
#     data = files.read()
#     words = data.split() 
#     dic = dict()
#     for word in words:
#         # count.setdefault(word,0)
#         dic[word] = dic.get(word,0) + 1
# pprint.pprint(dic)
        
# colors = ['red','yellow','green','orange'] 
# names = ['parker','programer','joe','riki','riki']

# k = dict(zip(colors,names))
# print(k)
# print(type(k))

# d = dict(enumerate(names))
# print(d)

# colors = ['red','green','blue','orange','white','white']

# d = dict() 
# for color in colors:
#        d[color] = d.get(color,0) + 1

# print(d)

# d = {'mathew':'blue','rachel': 'green','raymond':'red'} 
# while d:
#        key,value = d.popitem() 
#        print(key,value)


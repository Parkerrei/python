"""A string is sequence of unicode character wrapped inside single.
double,or triple quotes.
string in python is called array(collection) of bytes representing,
unicode characters. 
Square brackets cn be used to access elements of the string .
Each character of string can be indiviually access through the 
index of the string by using index()
the character of the string are given two way indices.
1,2,3,4, forward direction
-1,-2,-3,-4, backward direction

Traversing a string
Traversing mean iterating through the list of string,one
character at a time.using the index,u can traverse a string 
character by character
Membership operator (in) , (not in) will return boolean value True and False
They are used  with loop and condition to check for character in list ,
string,tuples."""

# standard character values
# [1]  +3*9-963=\dxc dzsawq1
# 3+63.36598*/8754210587/7410147to 9  --- 48-57
# [2] A to Z --- 65 - 90
# [3] a to z --- 97 - 122

# Function method in string :

# [1] isalnum(is alphabet numeric) search for alphabet n numbers in string.
# [2] isalpha()return True if all the character in string are alphabet.
# [3] isdigit()returns true if all character in string are digits.
# [4] islower()returns true if strings are in lower case.

# [5] isupper() checks for capitalize case.
# [6] isspace()checks if all character in strings are in white space.
# [7] lower()and upper()are use to convert strings to lower and upper respectively.
# [8] lstrip() returns left trim version of the string.
# [9] rstrip() returns right trim version of string.
# [10] strip() returns the trimed version of the string.
# [11] startswith() returns true if string starts with the specified value.
# [12] endswith() returns true if string ends with specified value.
# [13] title() convert the first character of each word to upper case.
# [14] istitle() returns true if the string follows the rules of a title.
# [15] replace() replace a string where a specified value is replaced with value.
# [16] join() concatenate reversed element with an empty string.
# [17] split() split the string with a specified separator and returns a list regardless of its class.
# [18] partition() convert list to tuple and divide the element into three part." 
# [19] find() use to parse substring and returns index of that subset it returns -1 if not found.
# str1 = 'we are programmers'
# # print(str.capitalize(str1))
# # print(str1.isupper())
# # print(str1.lower())
# # print(str1.upper())
# # print(str1.title())
# # k = str1.count(' ')
# # print(str1.isalnum())
# # print(str1.isalpha())
# # print(str1.strip('!'))
# # print(str1)
# print(str1.split())
# # print(type(str1))
# # print(str1.split())
# # print(type(str1))
# k = reversed(str1)
# print("".join(k))

# s = 'we are programmers'
# k = assert list(s)
# k[2] = 'p'
# m = " ".join(k)
# a = s[:2]+" "+"p" +s[3:]
# print(a)
  
# def remove_vowels(s):
#     vowels = 'a','e','i','o','u','A','E','I','O','U'
#     return  ''.join([char for char in s if char not in vowels])
# print(remove_vowels('hello'))
    
# def common(s):
#     d = dict() 
#     for char in s.strip():
#         d[char] = d.get(char,0) + 1  
#     return d
# string_2 = 'hello world' 
# print(common(string_2))

# def check_anagrams(s1,s2):
#     return sorted(s1) == sorted(s2) 
# print(check_anagrams('moon','noom'))

# def merge_sorted_lists(list1, list2):
#     merged_list = []
#     i, j = 0, 0
    
#     while i  < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1

#     merged_list.extend(list1[i:])
#     merged_list.extend(list2[j:])
#     return merged_list

# list1 = [1,2,4,7]
# list2 = [5,6,3,8]

# print(merge_sorted_lists(list1,list2))

# S = 'STRING' 
# print(type(S))
    
# K = ['STRING']
# print(type(K))

# user  = input('enter anything') 
# numbers = list(map(int,user.split()))
# print(user,numbers)

# user_input = input("Enter numbers separated by spaces: ")
# number_list =  int(user_input.split())
# print(f"The list of numbers is {number_list} and its type is {type(number_list)}")

# # Prompt the user for input
# user_input = input("Enter numbers separated by spaces: ")

# # Split the input string into a list of substrings
# input_list = user_input.split()

# # Use map() to convert each substring to an integer
# number_list = list(map(int, input_list))

# # Print the resulting list of integers
# print(number_list)

# listt = ['apple','mango','grapes','jooo'] 
# def swap(li,i1,i2):
#     li[i1],li[i2] = li[i2],li[i1] 
# swap(listt,2,1)
# print(listt)

# import os 
# def open_it(user):
#     if os.path.exists(user) :
#         try:
#             os.startfile(user) 
#         except Exception as e :
#             return e
#     else:
#         return 'file doesnot exist'
#     return user

# user = input('enter file name:') 
# print(open_it(user))



# import time 
# def celsius_(user):
#     return  (user * 9 / 5 ) + 32

# def fahrenheit_(user):
#     return (user - 32) * 5 / 9

# def main():
#     s = time.time()
#     while True:
#         print()
#         user1 = input('choose your conversion scale:\n1:  Celsius\n2:  Fahrenheit\nEnter:') 
      
#         if user1 != '1' and user1 != '2':
#             print('choos valid conversion scale...')
#             continue
        
#         elif user1 == '1':
#             try:
#                 user = float(input('your temperature:'))
#             except Exception :
#                 print('enter number only not characters ...') 
#             else:
#                 print(f'temperature in fahrenheit :{celsius_(user)}') 
#                 break

#         elif user1 == '2':
#             try:
#                 user = float(input('your temperature:'))
#             except Exception :
#                 print('enter numbers only not characters...') 
                
#             else:
#                 print(f'temperature in celsius :{fahrenheit_(user)}')
#                 break
            
#     e = time.time() 
#     print(f'{e-s:.2f} seconds')
# main()
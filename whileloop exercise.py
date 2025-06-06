# a while loop is a conditional loop that wil repeat the instructions with itself as long 
# as a conditional remains true.
# part of a loop:
# initialization ,testing(condition),body of the loop,update(re - initialization)


# def get_prime_factor(n):
#     factor = []
#     divisor = 2
#     while n > divisor:
#         if n % 2  == 0:
#             factor.append(divisor)
#             n = n//2
#         else:
#             divisor +=1
#         return divisor
# n = int(input("enter an integer"))
# print(get_prime_factor(n))

# """check prime numbers:"""
# n = int(input("enter number"))
# i = 2
# while i <=n:
#     flag = 0
#     for var in range(2,i):
#         if i % var == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(i,end = " ")
#         i += 1

# l,r,k = input().split()
# l = int(l)
# r = int(r)
# k = int(k)
# count = 0
# for i in range(l,r+1):
#     if i % k == 0:
#         count = count + 1
# print(count)

# while loop to print all even numbers between 1 to 20:
# i = 1  
# while i in range(0,21):
#     if i % 2 == 0:
#         print(i)
#     i += 1

# while loop to print sum of natural numbers:
# n = 10
# sum = 0
# i = 1
# while i in range(n+1):
#     sum = i + sum
#     i +=1
# print(sum)

# while loop to calculate factorial of a given no.
# n = int(input("enter a number for factorial calculation : "))
# i = 1
# factor = 1
# while i <=n:
#     factor *= i
#     i += 1
# print(factor)

# while loop to reverse a number:
# n = int(input("enter an integer : "))
# rever_value = 0
# while n > 0 :
#     last_digit = n % 10 
#     rever_value = last_digit + rever_value*10
#     n = n//10
# print(rever_value)

# while loop to find fibonacci sequence:
# n = 10
# fibo = [0,1]
# i = 2
# while i <= n :
#     next = fibo[i-1] + fibo[i-2]
#     fibo.append(next)
#     i +=  1
# print(fibo)

# find sum of even numbers using while loop :
# n = int(input("enter any number : "))
# sum = 0
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#         sum = sum + i
#     i +=1

# sum of digits using while loop:
# n = int(input("enter an integer : "))
# sum = 0
# while n > 0:
#     last_digit = n % 10
#     sum = sum + last_digit
#     n = n // 10
# print(sum)

# import random 
# user = int(input("enter number between 1 to 100: "))
# guess = random.randint(1,100)
# while user != guess:
#     break
# if user > guess:
#     print("too high")
# elif user < guess:
#     print("too low") 
# else:
#     print("congrats  u won hahahahah")
        
# while loop to print multiplication table of a given number. 
# i = 1
# n = 7
# while i <= 10:
#     print(n,"*",i,"=",n * i)
#     i += 1

# # for loop to print multiplication table:
# n = 10
# i = 1
# for  i in range(1,n+1):
#     print(n,"*",i,"=",n*i)
# while loop to check for prime number:
# n = int(input("enter an integer : "))
# k = len(str(n))
# i = 1 
# while i <=k:
#     if i % 2 ==0:
#         print("it\'s a composite number")
#     else:
#         print("it\'s a prime number")
#         break
# check avg using while loop:
# n = [1,23,3,1,2]
# k = len(n)
# i = 0
# sum = 0
# while i < k:
#     sum = sum + i
#     avg = sum // k
#     i += 1
# print(sum)

# n = int(input("enter an integer : "))
# s = ''
# while n>0:
#     r = n%2
#     s = str(r)+s
#     n = n//2
# print(s) 
# while loop to print sum of even  numbers:
# n = 1
# sum = 0
# while n <=10:
#     if n % 2 ==0:
#         sum = sum + n
#         print(sum)
#     n += 1
# while loop to print factor of a numer:
# # n = 4
# i = 1
# factor = 1
# while i <= n :
#     factor *= i
#     print(factor)
#     i +=1 

# # sum of current number and previous numbers:
# pre = 0
# for i in range(11):
#     sum = pre + i
#     print(sum)
#     pre = i

# # printing element at even index numbe:
# ste = input("enter string: ")
# for i in range(0,len(ste),2):
#     print(i)
# # remove first n characters from string:
# string = input("enter a string : ")
# n = int(input("enter no.of characters to remove :"))
# new = string[n:]
# print(new,'is the new string ')

# # remove first n characters from string:
# def remove_char(word,n):
#     print('original string :',word)
#     x = word[n:]
#     return x
# print(remove_char('prorgammer ',5))

# # check if first n last numbers are same:
# a = [12,22,3,1]
# for i in a:
#     if a[0] == a[-1]:
#         print(True)
#         break
#     else:
#         print(False)
#         break
# # counting no.of occurence of string:
# s = 'emma is a good developer .emma is a writer'
# p = s.count('emma')
# u = s.title()
# print(u)
# print(p)

# # printing pattern using for loop:
# for num in range(20):
#     for i in range(num):
#         print(num,end = ' ')
#     print('\n')

# # creating a new list adding odd from list1 n even from list2:
# list1 = [12,2,3,4]
# list2 = [22,3,2,1]
# list3 = []
# for i in list1:
#     if i % 2 != 0:
#         list3.append(i)
#         break
# for i in list2:
#     if i % 2 == 0:
#         list3.append(i)
#         continue
# print(list3)
# # calculate income tax:
# income = int(input("enter your  income amount in rs : "))
# tax = 0
# cess = 0
# for num in range(income):
#     if income <= 250000:
#         tax = 0
#     elif income <= 500000:
#         tax = (income - 250000)* 5 / 100
#     elif income <= 1000000:
#         tax = (income - 250000)* 20 / 100
#     else:
#         tax = (income-250000) * 30 / 100
#     print("tax =",tax)    
#     cess = tax * 4 / 100
#     print("cess = ",cess)
#     break

# # check for palindrome number:
# user = str(int(input("enter an integer  : ")))
# re = user[::-1]
# if user == re:
#     print(True,"its palindrome")
# else:
#     print(False,"its not palindrome")


# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j,end =' ')
#     print("\t\t")

# for num in range(11):
#     for i in range(num):
#         print(i,end = ' ')
#     print("\n") 

 
# for  i in range(6,0,-1):
#     for j in range(0,i-1):
#         print("*",end = ' ')
#     print(" ")


# l = int(input("enter a number : "))
# if l <=1:
#     print("not prime")
# else:
#     for k in range(2,int(l**0.5)+1):
#         if l % k == 0:
#             print("not prime")
#             break
#         else:
#             print("its prime")
# print(l)


t = (1,[2,4],{"x":4})
t[2]["y"] = t[0]
print(t)

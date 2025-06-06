
# total = 0
# count = 0
# average = 0
# for i in range(1,10+1):
#     total += i
#     count += 1
#     average = total / count
# print(total)
# print(count)
# print(average)

# l = [12,3,34,15,4,5]
# smallest = l[0]
# greater = l[0]
# for i in l:
#     if i < smallest:
#         smallest = i
#     elif i > greater:
#         greater = i
# print(smallest)
# print(greater)

# total = 0
# count = 0
# average = 0
# while True:
#     user = input('enter numbers:')
#     if user == 'done':
#         break
#     try:
#         user = int(user)
        
#     except ValueError:
#         print('enter valid numbers:')
    
#     else:
#         count += 1
#         total += user 
#         average = total/count
# print(count)
# print(total)
# print(average)
        
# class portfolio:
#     def __init__(self):
#         self.holdings  = {} 
        
#     def buy(self,ticker,shares):
#         self.holdings[ticker] = self.holdings.get(ticker,0) + shares  
        
#     def sell(self,ticker,shares):
#         self.holdings[ticker] = self.holdings.get(ticker,0) - shares
    
#     def __iter__(self):
#         return iter(self.holdings.items())

# p = portfolio() 
# p.buy('many',45)
# p.buy('groot',56)
# for (ticker , shares) in p:
#     print(ticker,shares)

# import itertools 

# ranks = list(range(2,11)) + ['j','q','k','a']
# ranks = [str(rank)for rank in ranks] 

# suits = ['hearts','clubs','diamonds','spades'] 
# deck  = [card for card in itertools.product(ranks,suits)] 

# # for (index,card) in enumerate(deck):
# #     print(1 + index ,card)

# hands = [hand for hand in itertools.combinations(deck,5)]
# print(f'number of 5 card poker hand is {len(hands)}')

# users = ['laust','parket','park','programmer'] 
# # for user in users:
# #     print(user)
# iterator_1 = iter(users) 
# print(iterator_1)

# import random 
# def random_walk(n):
#     x = 0 
#     y = 0

#     for _ in range(n):
#         step = random.choice(['n','s','e','w'])
#         if step == 'n':
#             y += 1 
#         elif step == 's':
#             y -= 1 
#         elif step == 'e':
#             x += 1 
#         else:
#             x -= 1 
#     return x,y 

# for i in range(25):
#     walk = random_walk(10)
#     print(walk,'distance from home = ',(walk[0]) + (walk[1]))

# from functools import reduce
# n = [33,55,6,100,56]
# k = reduce(lambda x,y: x if x > y else y,n)
# print(k)

# import time

# from numpy import square 
# s = time.time() 
# li  = [1,2,3,4] 
# k = square([x for x in li])
# print(k)
# e = time.time() 
# print(f'{e-s:.2f}seconds')


# a,b = -1,-3
# if a > 0 or b > 0:
#     flag = False 
#     print(flag)
# elif a <= 0 and b <= 0:
#     flag = True
#     print(flag)
# else:
#     print('draw')
# while True:
#     def check_status(a,b,flag):
#         if a <=0 or b > 0 and b <= 0 or a > 0 and not flag:
#             return True 
            
#         elif a < 0 and b < 0 and flag:
#             return True 
#         else: 
#             return False 
#     break
# print(check_status(1,0,True))

# def test_case():
#     user = int(input('enter number of test cases:'))
#     for _ in range(user):
#         a = int(input('enter a number :')) 
#         b = int(input('enter a number :'))
#         flag = bool(int(input('enter value for flag (0 for false , 1 for True)')))
#         print(check_status(a,b,flag))
# test_case()


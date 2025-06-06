# class student:
#     name = 'progammer'
# s1 = student() 
# print(s1.name)


# class student:
#     def __init__(self,names,marks):
#         self.names = names
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print('hello new progammers')
#     def get_avg(self):
#         sums = 0
#         for val in self.marks:
#             sums += val 
#         print('hello',self.names ,' ur average is ',sums/3)
# s1 = student('new progammers',[45,34,32])
# s1.get_avg()
# s1.hello()

# import time
# s = time.time() 
# class account:
#     def __init__(self,balance,account_no):
#         self.balance    = balance
#         self.account_no = account_no
        
#     def debit(self,amount):
#         self.balance -= amount 
#         print('Rs', amount,'was debitted') 
#         print('total balance',self.get_balance())
        
#     def credit(self,amount):
#         self.balance += amount
#         print('Rs',amount,'was creditted') 
#         print('total balance',self.get_balance())
    
#     def get_balance(self):
#         return self.balance

# acc1 = account(2345,123345345)       
# acc1.debit(100)
# acc1.credit(500)
# e = time.time() 
# print(e-s)

# bank account class
# import time 
# start_time = time.time() 
# class bankaccount():
#     def __init__(self,account_no,account_holder,balance):
#         self.account_no     = account_no
#         self.account_holder = account_holder 
#         self.balance        = balance 
        
#     def deposit(self,amount):
#         self.balance += amount
#         print('amount deposition is in process')
#         time.sleep(3)
#         print(f'Rs {amount} has been deposited \nCurrent balance is {self.balance}')
        
#     def withdrawal(self,amount):
#         self.balance -= amount
#         print('amount withdrawal is in proccess')
#         time.sleep(3)
#         print(f'amount deducted {amount} \nCurrent balance is {self.balance}')
       
#     def display_balance(self):
#         print('generating total balance')
#         time.sleep(3)
#         print(f'total balance remains Rs {self.balance}')
      
# b1 = bankaccount(234-345-656,'rei peter',3241)
# b1.deposit(int(input('enter amount u want to deposit: ')))
# b1.withdrawal(324)
# b1.display_balance()
# end_time = time.time()
# print(end_time - start_time)

# # (private and public objects or attributes)
# class friends():
#     def __init__(self,name1,name2):
#         self.__name1 = name1
#         self.name2 = name2
# # creating private methods and calling the private object inside it.
#     def __access(self):
#         print(self.__name1)
# # accessing private methods by creating public methods and calling private methods inside.
#     def gainaccess(self):
#         self.__access()
# # creating instance of class frienss.
# f1 = friends('jonny','nana')
# # calling public methods for private object.
# f1.gainaccess()

# inheritance
# class car:
#     name = 'progammer'  # class attributes
    
#     # @staticmethod
#     # def start():
#     #     print('car started ')
#     # @staticmethod 
#     # def stop():
#     #     print('car stopped')  
    
# class scorpio(car):
#     def __init__(self,name):
#         self.name = name
#     def st(self):
#         print(f'hello {self.name} welcome to progamming world')
#     # @classmethod
#     # def changename(cls,name):
#     #     cls.name = name
    
# car1 = scorpio(car)
# car2 = car()
# car1.st()

# print(car1.changename('jonny'))
# car1.changename('peter')
# car2 = car()
# car1.st()
# car2.start()

# class person:
#     name = 'peter'                        # class attributes
    
#     # def __init__(self,name):            # object / instance attributes
#     #     self.name = name   
    
#     # def changename(self,name):          # to change the class attributes contents
#     #     self.__class__.name = name 

#     @classmethod                          # methods to change class attributes contents
#     def changename(cls,name):             # instance methods
#         cls.name = name 
       
# p1 = person() 
# p1.changename('programmers') 
# print(person.name

# # multiple inheritence
# class a:
#     vara = 'welcome to class a'
# class b:
#     varb = 'welcome to class b'
# class c(a,b):
#     varc = 'welcome to class c'
# c1 = c() 
# print(c1.vara)
# print(c1.varb)

# class person:
#     def __init__(self,name):
#         self.name = name
    
#     # def changename(self,name):
#     #     self.__class__.name = 'rahu'
    
#     # @classmethod 
#     # def changename(cls,name):
#     #     cls.name = name
    
# p1 = person('peter') 
# print(p1.name)

# print(p1.name)
# print(person.name)

# # example of private method
# class message:
#     def __init__(self,p1,p2):                      # constructor 
#         self._person1 = p1 
#         self.person2 = p2 
        
#     def __hello(self):
#         return (f'hello {self._person1} how are u')
    
#     def inher(self):
#         return self.__hello()
        
# m1 = message('peter','jony')
# # print(m1.hello())
# print(m1.inher())

# class student:
#     def __init__(self,phy,math,sc):                  # constructor
#         self.phy  = phy 
#         self.math = math   
#         self.sc   = sc

#     @property                                  # decorator to change value of an atrributes
#     def percentage(self):
#         return str(self.phy + self.math + self.sc / 3) + '%'
    
# s1 = student(32,22,34) 
# s1.math = 23
# print(s1.percentage) 

# class animal:
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError('subclass must implement abstract method') 
    
# class dog(animal):
#     def sound(self):
#         return 'bark'
    
# class cat(animal):
#     def sound(self):
#         return 'meow' 
    
# animal1 = [dog(),cat()]
# for animal in animal1:
#     print(animal.sound())

# class complexs:                                 # example of polymorphism with code 
#     def __init__(self,real,img):
#         self.real = real 
#         self.img = img 

#     def shownumber(self):
#         print(self.real,'i +',self.img,'j') 
        
#     def __sub__(self,s):                          # dunder function 
#         r = self.real - s.real
#         p = self.img  - s.img
#         return complexs(r , p) 
    
# n1 = complexs(1,4) 
# n2 = complexs(2,3)
# n3 = n1 - n2 
# n1.shownumber()
# n2.shownumber()
# n3.shownumber()


# import math                                        # exercise for practising oops
# class circle:
#     def __init__(self,radius):
#         self.r = radius 
    
#     def area(self):
#         return math.pi * self.r**2
    
#     def perimeter(self):
#         return 2 * math.pi  * self.r
# c1 = circle(21) 
# print(c1.area()) 
# print(c1.perimeter())

# class employee:
#     def __init__(self,role,department,salary):
#         self.role       = role 
#         self.department = department 
#         self.salary     = salary 
        
#     def showdetails(self):
#         print('role       =',self.role)
#         print('department =',self.department)
#         print('salary     = Rs',self.salary)
    
# class engineer(employee):
#     def __init__(self):
#         # self.name = name 
#         # self.age = age 
#         super().__init__('engineer','it','32')
        
# e1 = employee('programer','webdev',1234)    
# e2 = engineer()
# e2.showdetails()
# print()
# e1.showdetails()

# import time 
# t = time.time()
# class animal:
#     def __init__(self,color,name):
#         self.color = color 
#         self.name = name 
    
#     def eat(self):
#         print(f'this is a {self.color} dog')
#         print(f'this is my  {self.name}')
        
#     def roar(self):
#         print(f'he was {self.color} in coat ')
#         print(f'{self.name}will kill u all')
        
# class cow(animal):
#     def __init__(self):
#         super().__init__('black','papa pig')

# class lion(animal):
#     def __init__(self):
#         super().__init__('yellow','samba')

# # c1 = cow() 
# # c1.eat()
# a1 = lion() 
# a1.roar()
# e = time.time() 
# print(f'elapsed time: {e - t:.2f}seconds')

# class order:
#     def __init__(self,item,price):
#         self.item = item 
#         self.price = price 
        
#     def __gt__(self,ord2):
#         return self.price > ord2.price

# or1 = order('chips',2)
# or2 = order('potato',12)
# print(or1 > or2 )

# class book:
#     def __init__(self,title, author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages 
    
#     def details(self):
#         print(self.title) 
#         print(self.author) 
#         print(self.pages) 
        
# b1 = book('harrypotter','j.k rowling',' 452')
# b1.details()

# class vehicle:
    # def __init__(self,make,model):                                 # inheritence 
#         self.make = make 
#         self.model = model   
        
# class car(vehicle):
#     def __init__(self,make,model,year):
#         super().__init__(make,model)
#         self.year = year
        
#     def details(self):
#         # print(f'maker = {self.make}\nmodel = {self.model}\nyear built = {self.year}')
#         print(f'make  = {self.make}')
#         print(f'model = {self.model}')
#         print(f'year  = {self.year}')
    
# v1 = car('ducati','ducati - m4',2023)
# v1.details()

# import math 
# class shape:
#     def __init__(self,area):
#         self.area = area 
    
#     def area(self):
#         raise NotImplementedError('sublclass must implement abstract method') 
    
# class rectangle(shape):
#     def __init__(self,height,width):
#         self.height = height 
#         self.width = width 
    
#     def shape(self):
#         return self.height * self.width 
    
# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius 

#     def area(self):
#         return math.pi * self.radius**2

# r1 = rectangle(12,23)
# print(r1.area())

# class car:
#     def __init__(self,make,model,year,color): 
#         self.make = make 
#         self.model = model 
#         self.year = year 
#         self.color = color 
#     def details(self):
#         print(f'made by = {self.make}')
#         print(f'model no = {self.model}') 
#         print(f'year built = {self.year}') 
#         print(f'color = {self.color}') 
# class car1(car):
#     def __init__(self,make,model,color,year):
#         super().__init__(make,model,color,year)
#         self.year = year
# c1 = car('ducati ','303','2012','blue') 
# c2 = car1('ducati','303','2012','red')
# c1.details()

# class animal:                                                                                                    # inheritence with overriding methods 
#     def __init__(self,name,species):
#         self.name = name 
#         self.species = species 
#     def details(self):
#       print('bow bow ')

# class dog(animal):
#     def __bow__(self,name,species):
#         super().__init__(name,species)                                                             
#     def details(self):
#         print('boooooo')
#         super().details()
        
# class cat(animal):
#     def __init__(self,name,species):
#         super().__init__(name,species)
#     def details(self):
#         print('meow meow')
#         super().details()

# a1 = animal('dog','wolf gang')
# a2 = dog('sheep','fox')
# a3 = cat('bully','were')
# a2.details()

# import math                       # example of inheriting and overriding methods / POLYMORPHISM
# class shape:
#     def __init__(self,area):
#         self.areas = area 
#     def area(self):
#         print(0)

# class rectangle(shape):
#     def __init__(self,area,width,height):
#         super().__init__(area)
#         self.height = height 
#         self.width  = width 

#     def area(self):
#         super().area()
#         print( self.height * self.width)
        
# class circle(shape):
#     def __init__(self,radius,area):
#         super().__init__(area)
#         self.radius = radius 
    
#     def area(self):
#         super().area()
#         print(math.pi * self.radius**2)
        
# s1 = shape(23) 
# r1 = rectangle(155,2,34)
# c1 = circle(23,7)
# s1.area()

# class bankaccount:                                                                                                           # ENCAPSULATION
#     def __init__(self,acc_no,balance):
#         self.acc_no = acc_no
#         self.balance = balance 

#     def deposit(self,user):
#         self.user = user 
#         print(f'money deposited :{self.balance + self.user} \nwithdraw money :{self.balance - self.user}\ntotal balance : {self.balance}'
# b1 = bankaccount(1343456,1234)
# b1.deposit(23)

# class item:
#     def __init__(self):
#         print('im god in disguise ')
#     def calculate_total_price(self,x,y):
#         return x * y   
    
# item1 = item() 
# item1.name = 'phone'
# item1.price = 100 
# item1.quantity = 5 
# print(item1.calculate_total_price(item1.price,item1.quantity))

# item2 = item() 
# item2.name = 'laptop' 
# item2.price = 1000 
# item2.quantity = 3 
# print(item2.calculate_total_price(item2.price,item2.quantity))

# class partyanimal():
#     x = 0
#     NAMe = 'hello world im a new in programming '
    
#     def __init__(self,nam):
#         self.name = nam
#         print(self.name,'constructed')
        
#     def party(self):
#         self.x = self.x + 2 
#         print(self.name,'party_count',self.x) 
        
# class footballfan(partyanimal):
#     def __init__(self,name,nam):
#         super().__init__(nam)
#         self.name = name
       
# j = footballfan('ladybug','ginger')
# print(j.NAMe)

                                          # LIBRARY MANAGEMENT SYSTEM
# class book:
#     def __init__(self,title,author,isbn):
#         self.title = title 
#         self.author = author 
#         self.isbn = isbn 
        
# class member:
#     def __init__(self,name, member_id):
#         self.name = name 
#         self.member_id = member_id 
        
# class Transaction:
#     def __init__(self,book,member,date_borrowed,date_returned = None):
#         self.book = book 
#         self.member = member 
#         self.date_borrowed = date_borrowed
#         self.date_returned = date_returned 

# class library:
#     def __init__(self):
#         self.books = [] 
#         self.members = [] 
#         self.transactions = [] 
    
#     def add_books(self,book):
#         self.books.append(book) 
    
#     def add_member(self,member):
#         self.members.append(member) 
    
#     def borrow_book(self,book,member,date_borrowed):
#         transactions = Transaction(book,member,date_borrowed)
#         self.transaction.append(transactions)
    
#     def return_book(self,book,member,date_returned):
#         for transaction in self.transactions:
#             if transaction.book == book and transaction.member == member and transaction.date_returned is None:
#                 transaction.data_returned = date_returned 
#                 break
# l1 = library() 
# print(l1.add_books('harry potter'))


#                                        E- COMMERECE PLATFORM 
# class product:
#     def __init__(self,name,price,stock):
#         self.name  = name 
#         self.price = price 
#         self.stock = stock 
# class customer:
#     def __init__(self,name,email):
#         self.name  = name 
#         self.email = email 

# class order :
#     def __init__(self,customer,product):
#         self.customer = customer 
#         self.product  = product 
#         self.total    = sum(product.price for product in product) 

# class Payment :
#     def __init__(self,order,payment_method):
#         self.order = order 
#         self.payment_method = payment_method

# class ECommercePLatform:
#     def __init__(self):
#         self.product = [] 
#         self.customers = [] 
#         self.orders = [] 
    
#     def add_product(self,product):
#         self.product.append(product) 
        
#     def add_customer(self,customer):
#         self.customers.append(customer)
    
#     def create_order(self,customerx,product):
#         Order = order(customer,product)
#         self.order.append(Order)
#         return order 
    
#     def process_payment(self,order,payment_method):
#         payment = Payment(order,payment_method) 
#         return payment 


#                          CHATT APLICATION 

# class user:
#     def __init__(self,username):
#         self.username  = username 
#         self.message = [] 
        
#     def send_message(self,chatroom,message):
#         chatroom.add_message(self,message)
    
# class Message:
#     def __init__(self,user,content):
#         self.user = user 
#         self.content = content 

# class ChatRoom:
#     def __init__(self,name):
#         self.name = name 
#         self.message = [] 
    
#     def add_message(self,user,content):
#         message = Message(user,content) 
#         self.message.append(message) 
    
# class Server:
#     def __init__(self):
#         self.Chatrooms = [] 
        
#     def create_chatroom(self,name):
#         chatroom = ChatRoom(name) 
#         self.chatroom.append(chatroom) 
#         return chatroom 
    
# s1 = user('pong') 
# print(s1.send_message('weboo','how are u'))

#                               BANKING SYSTEM 
# class Account:
#     def __init__(self,account_number,account_holder):
#         self.account_number = account_number
#         self.account_holder = account_holder 
#         self.balance = 0
    
#     def deposit(self,amount):
#         self.balance += amount 
    
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print('insufficient funds')
#         else:
#             amount -= self.balance 
#             print(f'your balance is {self.balance}')
            
# class customer: 
#     def __init__(self,name,customer_id):
#         self.name = name 
#         self.customer_id = customer_id 
        
# class Transaction:
#     def __init__(self,account,amount,transaction_type):
#         self.account = account 
#         self.amount = amount 
#         self.transaction_type = transaction_type 

# class Bank :
#     def _init_(self):
#         self.accounts = [] 
#         self.customers = [] 
        
#     def add_account(self,account):
#         self.accounts.append(account) 
    
#     def add_customer(self,customer):
#         self.customers.append(customer) 
    
#     def process_transaction(self,account,amount,transaction_type):
#         transaction = Transaction(account,amount,transaction_type)
#         if transaction == 'deposit':
#             account.deposit(amount) 
#         elif transaction == 'withdraw':
#             account.withdraw(amount)

# class dog:
#     attr1 = 'mamal'
#     attr2 = 'dog'
    
#     def fun(self):
#         print('im a ',self.attr1) 
#         print('im a ', self.attr2)  

# d1 = dog() 
# print(d1.attr1)
# d1.fun()

# def frequency_word(statement):
#     dictionary = dict() 
#     k = statement.split()
#     for item in k:
#         dictionary[item] = dictionary.get(item,0) + 1
#     return dictionary

# def multiple_test():
#     num_cases = int(input('enter number of test cases:')) 
#     for _ in range (num_cases):
#         statement = input('enter statement:') 
#         print(frequency_word(statement)) 
# multiple_test()


# class Monster :
#     health = 90 
#     energy = 40 
    
#     def __len__(self):
#         return 5
    
#     def __init__(self,health,energy):
#         self.health = health 
#         self.energy = energy 
        
#     def attack(self,amount):
#         print('the monster has attacked') 
#         print(f'{amount} of demage has been done')
#         self.energy -= 20 
#         print(self.energy) 
        
#     def move(something,speed):
#         print('the monster has moved') 
#         print(f'it has a speed of {speed}')

# m1 = Monster
# print(m1.attack(34))

# class fraction(object):
#     def __init__(self,num,denom):
#         assert  type(num) == int and type(denom) == int,
#         self.num = num 
#         self.denom = denom 

#     def __str__(self):
#         return str(self.num) + '/' + str(self.denom) 
    
#     def __add__(self,other):
#         top = self.numm * other.denom + self.denom * other.num 
#         bott = self.denom * other.denom 
#         return fraction(top,bott)
    
#     def __sub__(self,other):
#         top = self.num * other.denom - self.denom * other.num
         
# s = ['we are programmers']
# dictt = dict() 
# for char in s:
#     for x in char:
#         if not x == ' ' :
#             dictt[x] = dictt.get(x,0) + 1
# print(dictt)

# s = 'we are programmers' 
# dictt = dict() 
# for char in s:
#     if not char == ' ' :
#         dictt[char] = dictt.get(char,0) + 1 
# print(dictt)
    
# class customclass(list):
#     def __init__(self,*args):
#         # super().__init__(args) 
#         self.args = args
#     def sum(self):
#         return sum(self.args) 
    
# my_list = customclass(34,5,6,3)
# print(my_list.sum()

class animal:
    def __init__(self,moow):
        self.mow = moow
    def mow(self):
        return 'mow..mow...mow' 
    
class cat(animal):
    def mow():
        return 'meow...meow...'

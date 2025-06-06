# from statistics import mean as m 

# Admin = {"python":"12345","username":"password"}

# dictgrades = {"rishi":[23,34],
#               "peter":[55,51],
#               "pinky":[78,66]}

# def average():
#     for students in dictgrades:
#         students = dictgrades[students]
#         avg = m(students)
#         print("each student has an average of :", avg)

    
# def studentgrades():
#     studentname = input("enter student name: ")
#     gradedict = input("enter grade: ")
#     if studentname in dictgrades:
#         print("adding.....")
#         dictgrades[studentname].append(float[gradedict]) # type: ignore
#         print(dictgrades)
#     else:
#         print("student doesnot exist")
#         print(dictgrades)

# def removestudent():
#     name = input("enter student name: ")
#     if name in dictgrades:
#         del dictgrades[name]
#     else:
#         print("student doesnot exist")


# def main():
#     print("""weclome to the grading system
#     [1] - AVERAGE 
#     [2] - GRADE 
#     [3] - REMOVE STUDENT 
#     [4] - EXIT""")

#     LOG = input("enter what u want to do : ")

#     if LOG == "1":
#         average()
#     elif LOG == "2":
#         studentgrades()
#     elif LOG == "3":
#         removestudent()
#     elif LOG == "4":
#         exit()

# login = input("enter usename: ")
# password = input("enter password: ")

# if login in Admin:
#     if Admin[login] == password:
#         print("welcome", login)
#         while True:
#             main()
#     else:
#         print("enter valid password")
# else:
#     print("enter valid username")
    
#  l = int(input("enter  length "))
# n = int(input("enter no of photos to upload: "))

# while n>0:
#     w = int(input("enter width of photo: "))
#     h = int(input("enter height of photo: "))

#     if w < l or h < l:
#         print("upload another:")
#         print()
#     elif w > l or h > l:
#         if w == h:
#             print("acceted")
#             print()
#     else:
#         print("crop it")
#         print()
#     print(n)

# guess the number:
# import random
# r = random.randint(50,100)
# guess = 0
# while guess !=r:
#     guess = int(input("enter a number between 50 to 100 : "))
#     if guess > r:
#         print("to high :")
#     elif guess < r:
#         print("too low ")
# else:
#     print("number match congratulation")

# import random
# def main():
#     print("""welcome to the game chief : choose an option
      
#     1. play
      
#         2. exit """)
# main()
# user_input = int(input("enter your option : "))

# def user():
#     if user_input == "1":
#         play()
#     else:
#         exit()
# user()


# def play():       
#     action = input("enter any one (rock , paper, scissor):")
#     choices = ["rock","paper","scissors"]
#     computer_action = random.choice(choices)

#     if action == computer_action: 
#         print(f"it's a tie!")
#     elif(
#         (action =="rock" and computer_action == "scissors")
#     or  (action == "paper" and computer_action == "rock") 
#     or (action == "scissors" and computer_action == "paper")
#         ):
           
#         print(f'you win {action} beats {computer_action}')
#     else:
#         print(f'{computer_action} beats {action}')
# play()

# grid = [
#     ['.', '.', '.', '.', '.', '.'],
#     ['.', '5', '4', '.', '.', '.'],
#     ['6', '5', '4', '3', '.', '.'],
#     ['6', '5', '4', '3', '2', '.'],
#     ['.', '5', '4', '3', '2', '1'],
#     ['6', '5', '4', '3', '2', '.'],
#     ['6', '5', '4', '3', '.', '.'],
#     ['.', '5', '4', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.']
#     ]

# for y in range(len(grid[0])):
#     for x in range(len(grid)):
#         print(grid[x][y], end = '')
#     print()           

# generating numbers of head and tail :
# import random
# choose = ['head','tail']
# total = []
# streak = 6
# count = 0
# total_head = 0
# total_tail = 0

# for i in range(500):
#     k = random.choice(choose)
#     total.append(k)
    
# for i in range(len(total) - streak + 1):
#     if total[i:i + streak] == ['head'] * streak:
#         total_head += 1
#         count += 1
        
#     elif total[i:i + streak] == ['tail'] * streak:
#         total_tail += 1
#         count += 1
        
# print('no of flips',total)
# print(f'no of streaks of head is {total_head} and tail is {total_tail}',count)

# Conway's Game of Life
# import random, time, copy
# WIDTH = 60
# HEIGHT = 20

# # Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = [] # Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0,1) == 0:
#             column.append('#') # Add a living cell.
#         else:
#             column.append(' ') # Add a dead cell.
#     nextCells.append(column) # nextCells is a list of column lists.

# while True: # Main program loop.
#     print('\n\n\n\n\n') # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)

#     # Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end ='') # Print the # or space.
#         print() # Print a newline at the end of the row.

#     # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # Get neighboring coordinates:
#             # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#             leftCoord  = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT

#             # Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.

#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or
# numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ' '
#     time.sleep(1)

# The collatz sequence:

# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#     else:
#         result = 3 * number  + 1
#     print(result)
#     return result 

# def main():
#     while True:
#         try:
#             number = int(input("enter an integer :"))
#             while number != 1:
#                 number = collatz(number)
#         except ValueError:
#             print("enter valid number :")
            
# if __name__ =='__main__':
#     main()

# zigzag pattern :

# import time
# import sys
           
# indent = 0
# indentincreasing = True
                             
# try:
#     while True:
#         print('   ' * indent ,end = ' ')
#         print('&&&&&&&&&&&&&&&&&&')
#         time.sleep(0.4)

#         if indentincreasing:
#             indent += 1
#             if indent == 1:
#                 indentincreasing = False
#         else:
#             indent -= 1
#             if indent == 0:
#                 indentincreasing = True
                
# except KeyboardInterrupt:
#     sys.exit() 

# tic - tac - toe
# the_board = {'top-l':'','top-m':'','top-r':'',
#              'mid-l':'','mid-m':'','mid-r':'',
#              'low-l':'','low-m':'','low-r':''}

# def printboard(board):
#     print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
#     print('--++--')
#     print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
#     print('--++--')
#     print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
#     print('--++--')

# import time
# import cProfile
# profile = cProfile.Profile()
# profile.enable()
# time_ = time.time()
# # for i in range(1):
# for i in range(1,10+1):
#     for m in range(i):
#         print('-',end = ' ')
#     print()
#     time.sleep(0.5)
# for i in range(10,-1,-1):
#     for m in range(i):
#         print('-',end = ' ')
#     print()
#     time.sleep(0.5)
# profile.disable() 
# profile.print_stats()
# end_ = time.time()
# total_time = end_ - time_
# print(total_time)

# for i in range(10):
#     for k in range(10-i-1):
#         print(end = ' ')
        
#     for k in range(i+1):
#         print('-',end = ' ')
#     print()
# login system:

# import time 
# t = time.time()
# l = ['bible','harry potter','lord of the rings','amazon','50 shades of grey','40 laws of power']
# def prin(text,delay= 0.2):
#     for i , char in enumerate(text):
#         if i % 2 == 0 :
#             print(char.upper(),end = ' ' , flush = True )
#         else:
#             print(char.lower(),end = ' ' , flush = True )
#         time.sleep(delay)
# text = 'L💖O💖G💖I💖N💖'
# prin(text)
# print()

# def login():
#     while True:
#         admin = {'password':12345,'user_name':'python'}
#         user_name = input('enter user_name : ')
        
#         if user_name == admin['user_name']:
#             print('welcome ',user_name)
#         else:
#             print('invalid user_name ')
#             continue
#         print()
#         password = input('enter password : ')
#         if password == str(admin['password']):
#             print('welcome ', user_name)
#         else:
#             print('invalid password ')
#             continue

#         print()
#         for item , index  in enumerate(l):
#             print(item,index)
            
#         e = time.time() 
#         print(f'{e-t:.2f} seconds')
#         print('BYE BYE')
#         print()
#         break
# login()

import tkinter as tk
# Backend: Function to perform calculations
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error{e}"

# Frontend: Creating the GUI
def create_calculator():
    def on_button_click(char):
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + char)

    def on_equal_click():
        expression = entry.get()
        result = calculate(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    window = tk.Tk()
    window.title("Simple Calculator")

    entry = tk.Entry(window, width=16, font=('Arial', 24),borderwidth=0, relief='solid')
    entry.grid(row=0, column=0, columnspan=4)
    
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0
    for button in buttons:
        if button == '=':
            btn = tk.Button(window, text=button, width=3, height=6, command=on_equal_click)
        else:
            btn = tk.Button(window, text=button, width=4, height=2, command=lambda char=button: on_button_click(char))
        btn.grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    window.mainloop()

# Run the calculator
create_calculator()


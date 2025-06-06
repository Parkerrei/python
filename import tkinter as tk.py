'''in pygame the rect obect is used to manage the position and size of images (or any other rectangular objects).the x attributes 
of a Rect object controls the horizontal position ,while the y attributes controls the vertical  position.
Rect is used to define boundaries of an image , manipulate its position by moving left ,right ,up ,down,it is also used to detect collision between 
images
geometric transformation :methods like move(),inflate(),clip() allow for easy geometric transformation.
drawing and blitting: Rect object with the blit() methods makes it straightforward to draw images at specific positions.
using Rect objects  makes your code more readable and maintable by clearly defining the boundaries and position of objects..
in summary while we can manipulate  images directly using coordinates.Rect objects provides a structured and efficient way to handle 
positions,sizes and collisions,making your code  cleaner and more manageable.

collision using  rectangles : methods1 = rect1.colliderect(rect2))
method 2 = rect1.collidepoint(x,y)

MOST COMMONE EVENT TYPES IN PYGAME: 
1) QUIT
2) ACTIVEEVENT
3) KEYDOWN 
4) KEYUP
5) MOUSEMOTION
6) MOUSEBUTTONUP
7) MOUSEBUTTUONDOWN 
8) JOYAXISMOTION 
9) JOYBALLMOTION
10) JOYHATMOTION 
11) JOYBUTTONUP
12) JOYBUTTONDOWN
13) VIDEOSIZE 
14) VIDEOEXPOSE 
15) USEREVENT

PYGAME.DRAW METHODS 
1) PYGAME.DRAWRECT    -  IT DRAWS A RECTANGLE 
2) PYGAME.DRAWPOLYGON -  IT DRAWS A POLYGON 
3) PYGAME.DRAWCIRCLE  -  IT DRAWS A CIRCLE 
4) PYGAME.DRAWELLIPSE -  IT DRAWS A CRESCENT MOON SHAPE 
5) PYGAME.DRAWARC     -  IT DRAWS AN ARC 
6) PYGAME.DRAWLINE    -  IT DRAWS A LINE IN A SURFACE
7) PYGAME.DRAWLINES   -  IT DRAWS MULTIPLE LINE SEGMENTS 
8) PYGAME.DRAWAALINE  -  IT DRAWS A STRAIGHT ANTIALIASED LINE
9) PYGAME.DRAWAALINES -  IT DRAWS MULTIPLE STRAIGHT ANTIALIASED LINE SEGMENTS 

TRANSFORMATION METHODS IN PYGAME :
1) IT IS USE TO SCALE AN IMAGE 
2) IT IS USE TO ROTATE THE SURFACE '''



# import spacy
# import tkinter as tk 
# from tkinter import messagebox

# nlp = spacy.load('en_core_web_sm')
# class Todolist:
#     def __init__(self):
#         self.task = [] 
    
#     def add_task(self,task):
#         self.task.append({'task': task, 'completed':False})

#     def view_tasks(self):
#         for idx,task in enumerate(self.task,1):
#             status = 'Done' if task['completed'] else 'Not done'
#             print(f'{idx}, {task["task"]} - {status}') 
    
#     def mark_completed(self,task_id): 
#         if 0 < task_id <= len(self.task):
#             self.task[task_id - 1]['completed'] = True 
    
#     def delete_task(self,task_id):
#         if 0 < task_id <= len(self.task):
#             del self.task[task_id - 1] 
    
#     def save_task(self,file_name):
#         with open(file_name, 'w') as files:
#             for task in self.task:
#                 files.write(f"{task['task']},{task['completed']}\n")
            
#     def load_tasks(self,file_name):
#         try:
#             with open(file_name , 'r') as files:
#                 self.task = [] 
#                 for line in files: 
#                     task,completed = line.strip().split(',') 
#                     self.task.append({'task': task, 'completed': completed == 'True'})
#         except FileNotFoundError:
#             print('no saved tasks found.')

# def process_input(input_text):
#     doc = nlp(input_text) 
#     tasks = [chunk.text for chunk in doc.noun_chunks]
#     return tasks
    
# def add_task():
#     task = task_entry.get() 
#     if task != "":
#         todolist.add_task(task) 
#         update_task_list() 
#         task_entry.delete(0,tk.END)
#     else: 
#         messagebox.showwarning('warning', 'you must enter a task.')

# def delete_task():
#     try:
#         selected_task = task_listbox.curselection()[0] 
#         todolist.delete_task(selected_task + 1)
#         update_task_list()
#     except IndexError:
#         messagebox.showwarning('warning','you must enter a task.') 

# def update_task_list():
#     task_listbox.delete(0,tk.END)
#     for idx,task in enumerate(todolist.task,1):
#         status ='Done' if task['completed'] else 'Not done' 
#         task_listbox.insert(tk.END, f'{idx}, {task["task"]} - {status}') 

# root = tk.Tk() 
# root.title('Todolist') 
# root.geometry('400x400') 
# todolist = Todolist() 
# todolist.load_tasks('task.txt') 

# task_entry = tk.Entry(root,width = 30) 
# task_entry.pack(pady = 10) 


# add_button = tk.Button(root,text = 'add task',command = add_task) 
# add_button.pack(pady = 5) 

# delete_button = tk.Button(root, text = 'Delete task',command = delete_task) 
# delete_button.pack(pady = 5) 

# task_listbox  = tk.Listbox(root, width = 50, height = 10) 
# task_listbox.pack(pady = 10) 
# update_task_list() 
# root.mainloop()


# def main():
#     To_do_list = Todolist()
#     To_do_list.load_tasks('task.txt') 

#     while True: 
#         print('\n1. add Task\n2. View Task\n3. Mark Task as Completed\n4. Delete Task\n5. Save and exit')
#         choice = input('choose an option:')

#         if choice == '1':
#            task = input('enter the task:') 
#            To_do_list.add_task(task)

#         elif choice == '2':
#             To_do_list.view_tasks() 
            
#         elif choice == '3':
#             task_id = int(input('enter the task number to mark as completed:')) 
#             To_do_list.mark_completed(task_id) 
        
#         elif choice == '4':
#             task_id = int(input('enter the task number to delete:')) 
#             To_do_list.delete_task(task_id) 
        
#         elif choice == '5':
#             To_do_list.save_task('task.txt') 
#             break 
#         else:
#             print('Invalid choice. Please try again.') 

# if __name__== '__main__': 
#     main()



# import tkinter as tk 
# def display_text():
#     user_input = entry.get() 
#     label.config(text= user_input)
    
# # create main window
# root = tk.Tk()
# root.title('welcome to my first gui') 

# # creating an entry widget
# entry = tk.Entry(root)
# entry.pack() 

# # create a button for widgets
# button = tk.Button(root,text = 'click me',command = lambda:print('button click!'))
# button.pack()

# # create a label
# label = tk.Label(root,text = 'hello wrold!') 
# label.pack()

# # run the script using mainloop()
# root.mainloop()
 



# window = tk.Tk() 
# window.title('THis is my new window') 
# entry = tk.Entry(window)
# entry.pack()
# button = tk.Button(window,text = 'press ')
# button.pack()
# label = tk.Label(window,highlightcolor='blue',highlightthickness=90)
# label.pack(padx= 20,pady= 20)
# window.mainloop()


# def calculate(expression):
#     try:
#         result = eval(expression)
#         return result
#     except Exception as e:
#         return f"Error{e}"


# import pygame 
# from sys import exit

# pygame.init() 
# width , height= 700,500
# window = pygame.display.set_mode((width,height)) 
# pygame.display.set_caption('nuuuuuuuuuuuuub gaaaaaaaaaaaaaaaamer')
# clock = pygame.time.Clock()

# folder = 'D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//sky.png'
# folder3 = 'D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//ground.png'

# sky_surface = pygame.image.load(folder)
# ground_surface = pygame.image.load(folder3)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
            
#     window.blit(sky_surface,(0,0))
#     window.blit(ground_surface,(0,320))
   
#     pygame.display.update()
#     clock.tick(70)


from random import randint
import pygame 
from sys import exit
                          
def display_score():
    current_time  = int (pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'score : {current_time}',False,(45,45,45))
    score_rect    = score_surface.get_rect(center = (380,50))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 3

            screen.blit(snail1_surface,obstacle_rect)
        return obstacle_list
    else:
        return list()
      
pygame.init()
width , height = 800,400

screen  = pygame.display.set_mode((width,height))
pygame.display.set_caption('MY_FIRST__GAME')
time    = pygame.time.Clock()

test_font      = pygame.font.Font('D://park.py admin//py//font folder//UltimatePygameIntro-main//font//pixeltype.ttf',50)
game_name      = test_font.render('pixel bomber',False,'red')
game_name_rect = game_name.get_rect(center = (400,100))

game_active = True
start_time  = 0

sky_surface         = pygame.image.load('D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//sky.png').convert_alpha()
ground_surface      = pygame.image.load('D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//ground.png').convert_alpha()
                                                                                                                                     
player_surface      = pygame.image.load('D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//player//player_walk_1.png').convert_alpha()
player_rect         = player_surface.get_rect(midbottom = (100,300))
player_gravity      = 0

fly_surface         = pygame.image.load('D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//Fly//fly1.png').convert_alpha()
fly_rect = fly_surface.get_rect(center = (600,100))

player_stand        = pygame.image.load('D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//player//player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand,(340,300))
player_stand_rect   = player_stand_scaled.get_rect(center = (399,300))

snail1_surface      = pygame.image.load('D://park.py admin//py//graphics//UltimatePygameIntro-main//graphics//snail//snail1.png').convert_alpha()
snail1_rect         = snail1_surface.get_rect(midbottom = (500,300))

game_message        = test_font.render('press space to jump', False,'red')
game_message_rect   = game_message.get_rect(midtop = (400,40))

obstacle_rect_list = list()
obstacle_timer     = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()  
    
        if game_active:
            if event.type    == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if snail1_rect.colliderect(player_rect) or fly_rect.colliderect(player_rect):
                game_active = True
                snail1_rect.left = 800
                fly_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
        
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(snail1_surface,(snail1_rect))
        screen.blit(player_surface,(player_rect ))
        screen.blit(fly_surface,fly_rect)
        score = display_score()

        # SNAIL RECTANGLE IMAGE //// 
        # snail1_rect.x -= 4
        # if snail1_rect.right <= 0:
              # snail1_rect.left = 800
            
        # BIRD RECTANGLE IMAGE ////
        fly_rect.x -= 3
        if fly_rect.right <= 0:
            fly_rect.left = 800 

        # player gravity ////
        player_gravity += 1  
        player_rect.y  += player_gravity 
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        
        # bird collision////
        if fly_rect.colliderect(player_rect):
            game_active = False 
  
        # player collision ////
        if snail1_rect.colliderect(player_rect):
            game_active = False

        # obstacle
        obstacle_rect_list = obstacle_movement(obstacle_rect_list) 
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail1_surface.get_rect(midbottom = (randint(600 , 1100),300)))

    else:
        screen.fill((45,45,45))
        screen.blit(player_stand_scaled,player_stand_rect)
        screen.blit(game_name,game_name_rect)
        # screen.blit(game_message,game_message_rect)
        score_message      = test_font.render(f'your score : {score}',False,'dark blue')
        score_message_rect = score_message.get_rect(midbottom = (400,40)) 
        # screen.blit(score_message, score_message_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    time.tick(60)
    
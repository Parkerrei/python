
#     data = files.read() 
#     data  = data.upper() 
# with open('mbox-short.txt','w') as files:
#     files.write(data)
#     print(data)
    
    
# words = 'his e-mail is q-lar@freecodecamp.org'
# pi = words.split() 

# em = pi[3]
# pa = em.split('-')

# n = pa[1]
# print(n)


# with open('oop.txt') as files:
#     files.read() 
# print(files)

# l = [12,2,1,2,3,2]
# file_path = 'mbox-short.txt'
# with open(file_path,'w') as files:
#     for i in l:
#         files.write(file_path)
# with open('mbox-short.txt','r') as files:
#     files.read() 
#     print(files)

# file_path = 'hello world.txt'
# with open(file_path,'w') as files:
#     files.write('hello programmer we are one')
# print(file_path)

# # st = 'we are programmers and we are one'
# # with open('mbox-short.txt','r+') as files:
# #     for char in st:
# #         files.write(char)
# #     print(files)
# with open('mbox-short.txt','r') as files:
#     files.read() 
#     print(files)


# from pathlib import Path 
# myfiles = ['accounts.txt','details.csv','invite.docx']
# for filename in myfiles:
#     print(Path(r'c:\users\AI',filename))
#     print(filename)
    
# from pathlib import Path
# import os
# k = os.getcwd()
# print(k)
# c = Path.home() 
# print(c)

# with open('practise.txt', 'w') as files:
#     data = files.write('hi everyone\nwe are learning File I/O\nusing Java\nI like proramming in Java.')
#     print(data)
# new = 'python'
# old = 'Java'
# with open('file.txt','r') as files:
#     data = files.readline()
#     data = data.replace(old,new)
# with open('file.txt','r') as files:
#     data = files.read()
#     print(data)

# with open('programmer.txt','r') as files:
#     data = files.read() 
#     data = data.upper()
#     print(data)
# with open('progammer.txt','w') as files:
#     data = files.write(data)
#     print(data)

# import os 
# import shutil

# path = input('enter path:')
# files = os.listdir(path) 

# for file in files:
#     filename,extension = os.path.splitext(file)
#     extension = extension[1:]
    
#     if os.path.exists(path+'/' + extension):
#         shutil.move(path+'/'+file,path+'/'+extension+'/' +file)
#     else:
#         os.makedirs(path+'/'+extension)
#         shutil.move(path+'/'+file,path+'/'+extension+'/'+file)



#  import os 
# file_path = r'D:\park.py admin\py\images'
# if os.path.exists(file_path):
#    with open('bishop.png','r') as files:
#        data = files.read()
#        print(data)
    
# else:
#     print(f'{file_path} file dont exists')
# import os
# def get():
#     path = r'D:\park.py admin\py\server.py'
#     if os.path.exists(path):
#         os.startfile(path)
# #         with open('server.py','r') as files:
# #             data = files.read() 
# #             print('file exist',data)
# #     else:
# #         print('path doesnot exists>>>')
# get()
# help(get())
# string = 'hello im a new programmer'

# # string = ['hllo','world','im  ','a','new','programmer']
# lengths = map(len,string)
# print(list(lengths))


# import os 
# file = 'DSA.TXT' 
# if os.path.exists(file):
#     os.startfile(file)
#     # with open(file,'r') as files:
#     #     data = files.read() 
#     #     print(data) 
# else:
#     print('file doesnot exist')
 
# import os
# import time 
# import datetime

# remove = 'confidential' 
# if os.path.exists(remove):
#     print('you have 8 seconds to decides enter Y to pay and N for delete:')
#     times = datetime.datetime.now().strftime('%S')
#     print(times) 
#     time.sleep(1)
    
#     user = input('enter Y to pay N to delete files') 
#     if user == "N":
#         os.rmdir(remove) 
#         print('oops files deleted!:') 
#     elif user == "Y":
#         print('pay here') 
#     else:
#         print('timeout') 
        
    
# import shutil
# import os 
# folder = 'images'
# if os.path.exists(folder):
#     shutil.rmtree(folder) 
#     print('directory removed') 
# else:
#     print('folder doesnot exists')

# import os 
# os.removedirs('parent_folder')
# print('file removded')
 
# import os
# import time 

# # Directory where you want to create the files
# directory = 'my_files'

# # Create the directory if it doesn't exist
# if not os.path.exists(directory):
#     os.makedirs(directory)
    
# # Number of files to create
# # num_files = 5

# # Create multiple files
# for i in range(1, 5):
#     timestamp = time.time()
#     file_path = os.path.join(directory, f'file_{i}_{timestamp}.txt')
#     with open(file_path, 'w') as file:
#         file.write(f'This is file number {i} created at {timestamp}')

# print(f' {i} files created in {directory} directory.')

# import os 
# import shutil

# folder = 'my_files' 
# if os.path.exists(folder):
#     shutil.rmtree(folder) 
#     print('file removed') 
# else:
#     print('file doesnot exists')

# import os
# file = 'D:\\park.py admin\\py\\function.py'
# if os.path.exists(file):
#     os.startfile(file)
#     print('file transfer successful')
# else:
#     print('file doesnot exists')


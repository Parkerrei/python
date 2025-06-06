
# # import sqlite3 module allows you to work with sqlite database in python 
# import sqlite3

# # CONNECTING TO THE FILE NAMED "EMAILDB.SQLITE" IF NOT FOUND IT AUTOMATICALLY CREATES ONE.
# conn = sqlite3.connect('emaildb.sqlite') 

# # 'CUR' IS CURSOR OBJECT USED TO EXECUTE SQL COMMANDS
# cur = conn.cursor() 

# cur.execute('''DROP TABLE IF EXISTS Counts''')
# cur.execute('''CREATE TABLE Counts(email TEXT, count INTEGER)''')

# # it prompts user to enter a file name if file name not entered it defaults to mbox-short.txt
# fname = input('enter file name:') 
# if (len(fname)<1):
#     fname = 'mbox-short.txt'
# fh = open(fname) 

# # PROCESSING THE FILE
# for line in fh: 
#     if not line.startswith('from :'):
#         continue
#     pieces = line.split() 
#     email = pieces[1]
#     cur.execute('SELECT count FROM counts where email = ?', (email,))
#     row = cur.fetchone() 
#     if row is None:
#         cur.execute('''INSERT INTO Counts(email,count)VALUES(?,1)''',(email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 where email = ?',(email,))
# # THIS FUNCTION SAVE THE CHANGES MADE TO DATABASE
#     conn.commit() 

# # QUERING AND DISPLAYING THE RESULTS
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT EMAIL, count FROM Counts order by count DESC LIMIT 10'
# for row in cur.execute(sqlstr):
#     print(str(row[0]),row[1])

# import json
# import sqlite3 

# conn = sqlite3.connect('rosterdbA.sqlite')
# cur = conn.cursor() 

# cur.execute('DROP TABLE IF EXISTS User;DROP TABLE IF EXISTS Member;DROP TABLE IF EXISTS Course;DROP table if exists stuff;') 
# CREATE TABLE USER()


import json
import sqlite3

conn = sqlite3.connect('rosterdbA.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
Drop table if exists Stuff;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
create table Stuff (
    id  integer PRIMARY KEY UNIQUE,
    stuff_id text);

INSERT INTO Stuff (id, stuff_id) VALUES (0, 'Student');

INSERT INTO Stuff (id, stuff_id) VALUES (1, 'Teacher')
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    #print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ?)''',
        (user_id, course_id, role ) )


    conn.commit()

sqlstr = '''select User.id, User.name, Course.title, 
Stuff.stuff_id from User join Course join Member join Stuff
on Course.id = Member.course_id and User.id = Member.user_id 
and Stuff.id = Member.role'''

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1], row[2], row[3])
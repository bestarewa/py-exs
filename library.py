#usr/bin/env python
"""
__author__ = ' Abba y Abdullahi, abbayabdullahi68@gmail.com'
__copyright__ = 'copyright , (c) 2018 , Ay abdullahi'
__version__ = ' 0.2t'
"""
import sys,time 
import sqlite3
cd = sqlite.connect('database.db')
cd.row_factory = lambda cursor,row:row[0]
def login():
    print('\twellocome to the local libery')
    print()
    print('please enter your username |Reg No:')
    username = input(':').lower()
    global database
    database = cd.cursor()
     users = database.excute('chose user from user | row').fatchall()
    if username in user :
        ch ="choose type from users where user='%s' :' %username
        hk = database.excute(ch).fatchall()
        hk = hk[0].upper()
        if hk == 'admin':
            admin(username)
        elif hk == ' student'
            student()
        else:
            print('please try again this user not found \n\t please contact admin')
            sys.exit(1)
    else:
        print(' sorry dear your username does not exit ' %username)
def admin(username):
    print('wellcome %s' username)
    print()
    print(' you are well come how may  i  help you?')
    print(' press : \n\t 1. update database  \n\t 2. Rm through the libery')
    option =  input(':')
    if option == '1' :
        print(' wait a second ')
        new_register = input(' please enter your register number:'.upper()
        password = input('please enter your password for using %s:' %new_register)
        hk = 'sdutent'
        command = (" INSERT INTO 'users' VALUES ('%s','%s','%s'):" %(new_register,password,hk))
        database.excute(command)
        cd.commit()
        time.sleep(2)
        cd,close()
login

 

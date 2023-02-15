#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
while True:
    username = input('Enter a Username: ')
    password = input('Enter a password: ')
    text = []
    filename = open('C:\\Users\\dev\\Documents\\Python-Task\\capston-3\\user.txt','r+')
    text = filename.readlines()
    user,pas = False,False
    for i in range(len(text)):
        text1 = text[i].strip('\n').split(', ')
        u_name = text1[0]
        pwd = text1[1]
        #print(u_name,pwd)
        if username == u_name:
            user = True
        
        if password == pwd:
            pas = True
        
    if user == True and pas == True:
        print('You are successfully login')
        break
    elif user == True and pas == False:
        print('Incorrect password')
        print('Try again')
    elif user == False and pas == True:
        print('Incorrect usename')
        print('Try again')
    else:
        print('Incorrect usename and password')
        print('Try again')

filename.close()
#File open function
def file_open(filename):
    user_name = []
    file = open('filename','r+')
    for line in file.readline():
        user_name = line.strip('\n').split(',')

    return user_name
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r': #and username.lower == 'admin'
        while True:
            line = []
            username = input('Enter a Username: ')
            file = open('C:\\Users\dev\\Documents\\Python-Task\\capston-3\\user.txt','r+')
            #user_name = file_open('C:\\Users\dev\\Documents\\Python-Task\\capston-3\\user.txt','r+')
            for fline in file.readlines():
                line = fline.strip('\n').split(',')
                print(line[0])
            if username == line[0]:
                print('Username exist.Try another username')
            else:
                break
        while True:
            password = input('Enter a password: ')
            confirm_pass = input('Confirm a password: ')
            if password == confirm_pass:
                file = open('user.txt','a+')
                file.writelines('\n'+username+', '+password)
                line.append(username+', '+password)
                break
            else:
                print('Password Mismatch!')
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a':
        print('''Add the username of the person whom the task is assigned to,
        A title of a task,
        A description of the task and
        The due date of the task''')
        u_name = input('Enter a name whom the task is assigned to:  ')
        task = input('A title of a task:  ')
        detail_task = input('A description of the task:  ')
        due_date = input('The due date of the task: ')
        current_date = datetime.datetime.today()
        filetask = open('tasks.txt','a+')
        filetask.writelines(u_name+', '+ task+', '+ detail_task+', '+ str(current_date)+', '+ str(due_date)+', '+ 'NO'+'\n')
        filetask.close()
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        filetask = open('tasks.txt','r+')
        str_line = []
        print('=========================================================')
        for task in filetask.readlines():
            str_line = task.strip('\n').split(',')
            print('Task:             ', str_line[1])
            print('Assigned to:       ', str_line[0])
            print('Date assigned:    ', str_line[3])
            print('Due date:         ', str_line[4])
            print('Task complete?:   ', str_line[5])
            print('Task description: ', str_line[2])
            print('=========================================================')
           
        filetask.close()
        
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        f = open('C:\\Users\\dev\\Documents\\Python-Task\\capston-3\\tasks.txt','r+')
        #str_line,e_line,u_line = [],[],[]
        task = []
        contents = f.readlines()
        f.close()
        new_cont=[]
        for i in contents:
            print(i.split(',')[0])
            if username == i.split(',')[0]:
                new_cont.append(i) 
        
        for val,task in enumerate(new_cont):
            print(f'{val} . {task}')
        task_num = int(input('Please select the task number. : '))
        spilt_data = contents[task_num].split(', ')
        print(spilt_data)
        print('''Please select the option:\n
                1)Edit the task completion
                2)Edit the date
                ''')
        option = int(input(" : " ))
        if option == 1:
            spilt_data[5] = ' YES\n'
            join_data = ', '.join(spilt_data)
            contents[task_num] = join_data
        f= open('C:\\Users\\dev\\Documents\\Python-Task\\capston-3\\tasks.txt','w+')
        for line in contents:
            f.write(line)



        # for task in filetask.readlines():
        #     str_line = task.strip('\n').split(',')
        #     if username == str_line[0]:
        #         e_line.append(str_line[1])
        #         u_line.append(str_line)
        # print(u_line)
        # for count,val in enumerate(e_line) :
        #     print(count,val)
        # filetask.close()
        # fileobj = open('C:\\Users\\dev\\Documents\\Python-Task\\capston-3\\tasks.txt','a')

        # task_index= int(input("select the specific task: "))
        # print(f'task_index = {task_index}')

        # task_a = int(input("Select '1' to  mark the task complete or '2' to edit the date: "))
        # if task_a == 1:
        #     print(f'u_line[task_index] = {u_line[task_index]}')
        #     str_line[5] = 'HI \n'
        #     print(f'str_line = {str_line}')
        #     join_data = ','.join(str_line)
        #     print(f'join_data = {join_data}')
        #     print(f'u_line[task_index] = {u_line[task_index]}')
        #     u_line[task_index] = join_data
        #     print(f'u_line after changes = {u_line}')
        #     # for line in u_line:
        #     #     fileobj.write(line)
        #     #fileobj.write('u_line'.join( str_line[5].replace('NO','YES')))
        #     #print(fileobj)
        # elif task_a == 2:
        #     print(u_line[task_index])
        #     if ' YES' in u_line[task_index]:
        #         print('Task is completed No need of editing')
        #     else:
        #         u_line[4] = input('Enter the new due date: ')
        # elif task_index == -1:
        #     print('Go To menu')

        # # no_task = len(count)
        # # for i <= no_task :

        # fileobj.close()
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
file.close()       
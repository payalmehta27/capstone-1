#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime, os, time, stat

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
dir='/Users/c_kmehta/capston/capstone-1'
os.chdir(dir)
def menu(username):
    if username == 'admin':
        menu_input = input('''
        Select one of the following Options below:
        r   - Registering a user
        a   - Adding a task
        va  - View all tasks
        vm  - view my task
        gr  - generate reports
        ds  - display statistics
        e   - Exit: 
        ''').lower()
    else:
        menu_input = input('''
        Select one of the following Options below:
        r   - Registering a user
        a   - Adding a task
        va  - View all tasks
        vm  - view my task
        e   - Exit: 
        ''').lower()
        
    if menu_input.lower() == "r":
        add_user(username)
            
    elif menu_input.lower() == "a":
        add_task()
        
    elif menu_input.lower() == "va":
        view_all()
        
    elif menu_input.lower() == "vm":
        view_mine()
        
    elif menu_input.lower() == "ds":
        display_statistics()

    elif menu_input.lower() == "gr":
        generate_reports()

    elif menu_input.lower() == "e":
        exit(1)      

    else:
        print("Your menu_input did not meet a menu item. Please try again.\n")

def add_task():
    print('''Add the username of the person whom the task is assigned to,
        A title of a task,
        A description of the task and
        The due date of the task''')
    u_name = input('Enter a name whom the task is assigned to:  ')
    task = input('A title of a task:  ')
    detail_task = input('A description of the task:  ')
    due_date = input('The due date of the task: ')
    today = datetime.datetime.today()
    current_date = today.strftime("%d %b %Y")
    with open('tasks.txt','a+') as f:
        f.write(u_name+', '+ task+', '+ detail_task+', '+ str(current_date)+', '+ str(due_date)+', '+ 'NO'+'\n')
        print('Task added.')
        menu(username)
    
def user_check():
    users = {}
    with open("user.txt", "r") as f:
        for line in f:
            user_check = line.strip("\n")
            if user_check != "":
                user_check = user_check.split(", ")
                users.update({user_check[0]: user_check[1]})
    return users

def check_task():
    tasks = []
    count = 1
    with open("tasks.txt", "r") as f :
        for line in f :
            task_check = line.strip("\n")
            if task_check != "" :
                task_check = [task_check.split(", ") + [count]]
                tasks.extend(task_check)
                count += 1
    return tasks

def add_user(username):
    if username != 'admin':
        print("You do not have permission to perform this action.\n")
        menu(username)
    else:
        token=True
        while (token):
            new_user = input("Please enter the username you would like to add: ")
            user_list = user_check()
            if new_user in user_list:
                print("That username aleray exist, please try a different username.\n")
            else:
                new_pass = input('Enter a unique password: ')
                confirm_pass = input('Confirm your password: ')
                if new_pass == confirm_pass:
                    with open("user.txt", "a") as f:
                        f.write(f"\n{new_user}, {new_pass}")
                        print(f"new user {new_user} has been added!")
                        print()
                        token = False
                        menu(username)
                else:
                    print('Password Mismatch!')
def view_all():
    with open('tasks.txt','r+') as f:
        str_line = []
        print("="*60)
        for task in f.readlines():
            str_line = task.strip('\n').split(',')
            print('Task:             ', str_line[1])
            print('Assigned to:       ', str_line[0])
            print('Date assigned:    ', str_line[3])
            print('Due date:         ', str_line[4])
            print('Task complete?:   ', str_line[5])
            print('Task description: ', str_line[2])
            print("="*60)
            print()
        menu(username)

def view_mine():
    contents,actual_line,j = [],{},0
    tasks = check_task()
    for i in range(len(tasks)):
        if username == tasks[i][0]:
            actual_line[j] = tasks[i][6]
            j+=1
            contents.append(tasks[i][1])

    for val,task in enumerate(contents):
        print(f'{val}. {task}')

    task_num = int(input('Please select the task number: '))
    spilt_data = contents[task_num].split(', ')
    print(f'spilt_data = {spilt_data}')
    print('''Please select the option:\n
            1)Edit the task completion
            2)Edit the date
            ''')
    option = int(input(": " ))
    if option == 1:
        line_num=actual_line[task_num]
        tasks = check_task()
        string_task = ""
        for i in range(0, len(tasks)):
            if line_num == tasks[i][6]:
                tasks[i][5] = "Yes"
            tasks[i].pop()
            string_task += ", ".join(tasks[i]) + "\n"
        with open("tasks.txt", "w") as f :
            f.write(string_task)
        menu(username)
    elif option == 2:
        print('''Please select the option:\n
                 1) Edit by username
                 2) Edit by due date
            ''')
        edit_option = int(input("Enter your option: " ))
        if edit_option == 1:
            string_task = ""
            line_num=actual_line[task_num]
            edit_user = input('Editing Username:  ')
            if edit_user in user_check():
                for i in range(len(tasks)) :
                    if line_num == tasks[i][6] :
                        tasks[i][0] = edit_user

                    #Remove number added in as part of task_check() function
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                with open("tasks.txt", "w") as f :
                    f.write(string_task)
                menu(username)
            else :
                print("Username does not exist\n")
                menu(username)
        elif edit_option == 2:
            string_task = ""
            line_num=actual_line[task_num]
            edit_duedate = input("Please enter due date in dd mmm yyyy format:\n")
            for i in range(len(tasks)) :
                if line_num == tasks[i][6] :
                    tasks[i][4] = edit_duedate
                tasks[i].pop()
                string_task += ", ".join(tasks[i]) + "\n"
            with open("tasks.txt", "w") as f :
                f.write(string_task)
            menu(username)

def select_task():
    tasks = check_task()
    select_task = True
    while(select_task):
        task_number = input("Please enter your task reference or '-1' to return to menu:\n")
        try :
            task_number = int(task_number)
        except :
            print("Invalid input\n")
        if task_number == -1 :
            print()
            menu(username)
        else :
            for i in range(0, len(tasks)) :
            #If user and assigned_user are the same plus task_number matches task reference, alow user to edit task or mark complete
                if task_number == tasks[i][6] and tasks[i][5].lower() == "yes" :
                    print(f"task reference {task_number} is already complete, no further editing is permitted\n")
                    
                elif username == tasks[i][0] and task_number == tasks[i][6] :
                    modify_or_complete = input('''Please select the option:\n
                1)Edit the task completion
                2)Edit the due date
                ''')
                    print()

                    if modify_or_complete.lower() != '1' and modify_or_complete.lower() != '2' :
                        print("Invalid input.\n")

                    elif modify_or_complete.lower() == '1' :
                        mark_task(task_number)
                        return

                    else :
                        edit_task(task_number)
                        return

def mark_task(task_number) :
    tasks = check_task()
    string_task = ""
    for i in range(0, len(tasks)) :
        if task_number == tasks[i][6] :
                   tasks[i][5] = "Yes"
        tasks[i].pop()
        string_task += ", ".join(tasks[i]) + "\n"
    with open("tasks.txt", "w") as f :
        f.write(string_task)

def edit_task(task_number) :
    tasks = check_task()
    user_list = user_check()
    string_task = ""
    editing = True
    
    #Check if user would like to edit assigned person or due date
    while(editing) :
        user_or_date = input("Please enter 'user' to edit task assignment, 'date' to edit due date or 'both' to edit both:\n")
        if user_or_date.lower() == "user" :
            #Have user enter newly assigned user, checking that username exists
            new_user = input("Please enter the username to which this task should be assigned:\n")
            if new_user in user_list :
                for i in range(0, len(tasks)) :
                    if task_number == tasks[i][6] :
                        tasks[i][0] = new_user

                    #Remove number added in as part of task_check() function
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                editing = False
            else :
                print("Username does not exist\n")

        #have user enter in new due date         
        elif user_or_date.lower() == "date" :
            new_date = input("Please enter when the task is due in dd mmm yyyy format:\n")
            for i in range(0, len(tasks)) :
                if task_number == tasks[i][6] :
                    tasks[i][4] = new_date
                tasks[i].pop()
                string_task += ", ".join(tasks[i]) + "\n"
                editing = False

        #Have user enter new assigned user, checking that username exists, and enter new due date                
        elif user_or_date.lower() == "both" :
            new_user = input("Please enter the username to which this task should be assigned:\n")
            if new_user in user_list :
                new_date = input("Please enter when the task is due in dd mmm yyyy format:\n")
                for i in range(0, len(tasks)) :
                    if task_number == tasks[i][6] :
                        tasks[i][0] = new_user
                        tasks[i][4] = new_date
                    tasks[i].pop()
                    string_task += ", ".join(tasks[i]) + "\n"
                    editing = False
            else :
                print("Username does not exist\n")

    #Open "tasks.txt" file in write mode and write the variable "string_task" to it
    with open("tasks.txt", "w") as f:
        f.write(string_task)

def display_statistics() :
    old_file = True
    if (os.path.exists('./task_overview.txt') == False) or (os.path.exists('./user_overview.txt') == False) :
        generate_reports()
    else :
        task_time = os.stat('task_overview.txt')
        task_time = time.ctime(task_time[stat.ST_MTIME])
        user_time = os.stat('user_overview.txt')
        user_time = time.ctime(user_time[stat.ST_MTIME])
        print(f"task_overview.txt was last modified {task_time} and user_overview.txt was last modified {user_time}")
        while(old_file) :
            regenerate = input("Would you like to update the files before proceeding? y/n\n")
            print()
            if regenerate.lower() == "y" :
                generate_reports()
                print()
                old_file = False
            elif regenerate.lower() == "n" :
                old_file = False
            else :
                print("invalid input\n")

    #Print both files to the screen
    with open('task_overview.txt', 'r') as f:
        for line in f :
            print(line, end = '')

    print()

    with open('user_overview.txt', 'r') as g:
        for line in g :
            print(line, end = '')
    print()
    menu(username)

def generate_reports() :
    task = check_task()
    users = user_check()
    users = [*users]
    total = len(task)
    total_users = len(users)
    complete = 0
    incomplete = 0
    overdue = 0
    percent_incomplete = 0
    percent_overdue = 0

    #Find and keep count of all tasks, incomplete tasks and overdue tasks
    for i in range(0, total) :
        if task[i][5].lower() == "yes" :
            complete += 1
        elif task[i][5].lower() == "no" and datetime.datetime.strptime(task[i][4], '%d %b %Y') < datetime.datetime.now():
            incomplete += 1
            overdue += 1
            percent_incomplete = (incomplete / total) * 100
            percent_overdue = (overdue / total) * 100
        
        elif task[i][5].lower() == "no" :
            incomplete += 1
            percent_incomplete = (incomplete / total) * 100
            
    #Generate "task_overview.txt" file in an easy to read manner
            
    with open("task_overview.txt", "w") as f :
        f.write(f"Number of tasks\t\t- {total}\n")
        f.write(f"Number completed\t- {complete}\n")
        f.write(f"Number incomplete\t- {incomplete}\n")
        f.write(f"Number overdue\t\t- {overdue}\n")
        f.write(f"Percentage incomplete\t- {percent_incomplete:.2f}%\n")
        f.write(f"Percentage overdue\t- {percent_overdue:.2f}%\n")

    #Generate "user_overview.txt" filen an easy to read manner
        
    with open("user_overview.txt", "w") as g :
        g.write(f"Total users\t- {total_users}\n")
        g.write(f"Total tasks\t- {total}\n\n")

        #Loop through users to seperate tasks by their specific assigned user
        
        for i in range(0, total_users) :
            
            #Local variables declared within for loop to prevent double counting from occuring
            
            user_tasks = 0
            completed = 0
            not_complete = 0
            user_overdue = 0
            task_percent = 0
            complete_percent = 0
            incomplete_percent = 0
            overdue_percent = 0

            #Loop through specific user tasks to find completion status and due dates. Count of number of tasks, completed or not and due date maintained
            
            for j in range(0, total) :
                if users[i] == task[j][0] and task[j][5].lower() == "yes":
                    user_tasks += 1
                    completed += 1
                    
                #datetime.datetime.strptime(input, format) converts the string format date into a date object format, allowing comparison against the current time
                #obtained via datetime.datetime.now(). datetime.today unsuitable due to the time element not generating as was present in teh strptime() method
                    
                elif users[i] == task[j][0] and task[j][5].lower() == "no" and datetime.datetime.strptime(task[j][4], '%d %b %Y') < datetime.datetime.now():
                    user_tasks += 1
                    not_complete += 1
                    user_overdue += 1
                    

                elif users[i] == task[j][0] and task[j][5].lower() == "no" :
                    user_tasks += 1
                    not_complete += 1
                    
                #Calculate user percentages, ensuring that 0 assigned tasks does not result in a divide by 0 error
                    
                task_percent = (user_tasks / total) * 100
                if user_tasks != 0 :
                    complete_percent = (completed / user_tasks) * 100
                    incomplete_percent = (not_complete / user_tasks) * 100
                    overdue_percent = (user_overdue / user_tasks) * 100
                    
            #Write the results to the file before progressing to the next registered user        
            g.write("-" * 50 + "\n")
            g.write(f"User: {users[i]}\n\n")
            g.write(f"Number of user tasks\t\t- {user_tasks}\n")
            g.write(f"Percentage of total tasks\t- {task_percent:.2f}%\n")
            g.write(f"Percentage completed\t\t- {complete_percent:.2f}%\n")
            g.write(f"Percentage incomplete\t\t- {incomplete_percent:.2f}%\n")
            g.write(f"Percentage overdue\t\t- {overdue_percent:.2f}%\n")
    menu(username)

def login():
    for i in range(3):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        user_list = user_check()
        
        if username in user_list and user_list.get(username) == password:
            return username
        else:
            print("Your username and/or password is incorrect, please ensure your caps lock is off and try again.\n")
        
        if i == 2:
            exit(1)
        
while True:
    token = True
    username = login()
    menu(username)

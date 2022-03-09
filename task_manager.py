from datetime import datetime

login = False

# Provide menu options

admin_menu = '''
Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
s - statistics
e - exit
Selection: '''

user_menu = '''
Please select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
Selection: '''

# Login

while not login:

    # Ask user input

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_input = f"{username}, {password}"
    menu_selection = ""

    # Open the txt file and read and create a valid
    with open("user.txt", "r") as valid:

        valid = valid.read()
        if user_input == "admin, adm1n":
            login = True
            print("\nLogin successful!")
            menu_selection = input(admin_menu)

        elif user_input in valid:
            login = True
            print("\nLogin successful!")
            menu_selection = input(user_menu)

        else:
            print("\nThe login details entered are invalid. Please try again.\n")


# Admin menu

def admin_menu():
    menu_selection = input('''
    Please select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    s - statistics
    e - exit
    Selection: ''')

    # Register user if admin only

    if (menu_selection == "r") and (username == "admin"):
        reg_user()

    # Add task

    if menu_selection == "a":
        add_task()

    # View all tasks

    if menu_selection == "va":
        view_all()

    # View my tasks

    if menu_selection == "vm":
        view_mine()

    # Statistics

    if menu_selection == "s":
        insert_report()

    # Generate report

    if menu_selection == "gr":
        from datetime import datetime
        with open("tasks.txt", "r") as generate_report:
            generate_report = generate_report.readlines()
            task_total = 0
            completed_tasks = 0
            uncompleted_tasks = 0
            due_dates = 0
            overdue_tasks = 0
            incomplete_perc = 0
            overdue_perc = 0

            with open("task_overview.txt", "w") as task_overview:
                for gr in generate_report:
                    gr = gr.strip("\n").split(", ")
                    due_dates = datetime.strptime(gr[4], "%d %b %Y")
                    task_total += 1

                    if gr[5] == "Yes":
                        completed_tasks += 1
                    else:
                        uncompleted_tasks += 1

                    if (datetime.today() > due_dates) and (gr[5] == "No"):
                        overdue_tasks += 1

                incomplete_perc = round((uncompleted_tasks / task_total) * 100, 2)
                overdue_perc = round((overdue_tasks / task_total) * 100, 2)

                # Write to txt file

                task_overview.write(f'''Task Overview:
                                Task total:\t\t\t\t {task_total}
                                Completed Tasks:\t\t\t {completed_tasks}
                                Uncompleted Tasks:\t\t\t {uncompleted_tasks}
                                Overdue Tasks:\t\t\t\t {overdue_tasks}
                                Incomplete Task Percentage:\t\t {incomplete_perc}%
                                Overdue Task Percentage:\t\t {overdue_perc}%''')

                # Print to user

                print(f'''
                        Your Task Overview has successfully been updated as follows:
                        Task Overview:
                        Task total:\t\t\t\t {task_total}
                        Completed Tasks:\t\t\t {completed_tasks}
                        Uncompleted Tasks:\t\t\t {uncompleted_tasks}
                        Overdue Tasks:\t\t\t\t {overdue_tasks}
                        Incomplete Task Percentage:\t\t {incomplete_perc}%
                        Overdue Task Percentage:\t\t {overdue_perc}%''')

        # user_overview

        with open("user_overview.txt", "w") as user_overview:
            with open("user.txt", "r+") as user_report:
                user_report = user_report.readlines()
                with open("tasks.txt", "r+") as task_report:
                    task_report = task_report.readlines()

                    for ur in user_report:
                        ur = ur.split(", ")[0]
                        user_count = 0
                        task_count = 0
                        user_task_total = 0
                        user_task_perc = 0
                        task_comp = 0
                        task_incomplete = 0
                        user_perc_complete = 0
                        user_perc_incomplete = 0
                        inc_overdue = 0
                        perc_inc_overdue = 0

                        user_count += 1

                        for tr in task_report:
                            tr = tr.strip("\n")
                            task_count += 1
                            if tr.startswith(ur):
                                if tr.endswith("Yes"):
                                    task_comp += 1
                                if tr.endswith("No"):
                                    task_incomplete += 1
                                if (tr.endswith("No")) and (datetime.today() > due_dates):
                                    inc_overdue += 1
                                user_task_total += 1

                        if user_task_total != 0:
                            user_task_perc = round((user_task_total / task_count) * 100, 2)
                        else:
                            user_task_perc = 0

                        if task_comp != 0:
                            user_perc_complete = round((task_comp / user_task_total) * 100, 2)
                        else:
                            user_perc_complete = 0

                        if task_incomplete != 0:
                            user_perc_incomplete = round((task_incomplete / user_task_total) * 100, 2)
                        else:
                            user_perc_incomplete = 0

                        if inc_overdue != 0:
                            perc_inc_overdue = (inc_overdue / user_task_total) * 100
                        else:
                            perc_inc_overdue = 0

                        # Write to txt file

                        user_overview.write(f'''
                                            {ur} Report:
                                            Total Tasks:\t\t\t\t {user_task_total}
                                            Percentage Tasks assigned:\t\t {user_task_perc}%
                                            Percentage completed:\t\t\t {user_perc_complete}%
                                            Percentage incomplete:\t\t\t {user_perc_incomplete}%
                                            Percentage incomplete and overdue:\t {perc_inc_overdue}%
                                            ''')

                        # Print to user

                        print(f'''
                            {ur} Report:
                            Total Tasks:\t\t\t\t {user_task_total}
                            Percentage Tasks assigned:\t\t {user_task_perc}%
                            Percentage completed:\t\t\t {user_perc_complete}%
                            Percentage incomplete:\t\t\t {user_perc_incomplete}%
                            Percentage incomplete and overdue:\t {perc_inc_overdue}%
                            ''')

            # Statistics

            if menu_selection == "s":
                insert_report()

                # User Stats

                user_stat_list = []
                user_stat_total = 0
                with open("user_overview.txt", "r") as user_stats:
                    user_stats = user_stats.readlines()
                    for us in user_stats:
                        us = us.strip().split("\t ")
                        user_stat_list.append(us)

                    for ust in user_stat_list:
                        if "Total Tasks:\t\t\t" in ust:
                            user_stat_total += 1
                    print(f"Users:\t\t\t {user_stat_total}")

                # Task stats

                task_stat_list = []
                task_stat_total = 0
                with open("task_overview.txt", "r") as task_stats:
                    task_stats = task_stats.readlines()
                    for ts in task_stats:
                        ts = ts.strip().split("\t ")
                        task_stat_list.append(ts)

                    for tst in task_stat_list:
                        if "Task total:\t\t\t" in tst:
                            task_stat_total = tst[1]
                print(f"Tasks:\t\t\t {task_stat_total}")

                # Exit

                if menu_selection == "e":
                    print("\nYou have successfully logged out.")


# User menu
def normal_menu():
    option_selection = input('''
                        Please select one of the following options:
                        a - add task
                        va - view all tasks
                        vm - view my tasks
                        e - exit
                        Selection: ''')

    if menu_selection == "a":
        add_task()

    if menu_selection == "va":
        view_all()

    if menu_selection == "vm":
        view_mine()

    if menu_selection == "e":
        print("\nYou have successfully logged out.")


# Register user

def reg_user():
    new_username = ""
    new_password = ""
    confirm_password = ""
    users = []
    user_check = False

    with open("user.txt", "r+") as user_info:
        new_username = input("\nEnter your new username: ")
        new_password = input("Enter your new password here: ")
        confirm_password = input("Confirm your new password: ")

        for q in user_info:
            if new_username in q:
                user_check = True

    with open("user.txt", "a") as user_info:
        if user_check:
            print("\nThis username is already taken")
            reg_user()

        elif new_password == confirm_password:
            user_info.write(f"\n{new_username}, {new_password}")
            print("\nNew user successfully added!")

        else:
            print("\nYou did not confirm the correct password. Please try again.")
            reg_user()


# Add tasks

def add_task():
    with open("tasks.txt", "a") as task_info:
        task_username = input("\nEnter the username of the person you would like to assign the task to: ")
        task = input("Enter your task title here: ")
        task_description = input("Enter a description of your task here: ")
        assigned_date = datetime.date.today().strftime("%d-%b-%Y").replace("-", " ")
        due_date = input("Enter your task due date here, in format as day-month-year: ")
        task_complete = "No"
        print(f"\nYour task has successfully been assigned to {task_username}.")

        task_info.write(f"\n{task_username}, {task}, {task_description}, {assigned_date}, {due_date}, {task_complete}")


# View all tasks

def view_all():
    with open("tasks.txt", "r+") as all_tasks:
        for tasks in all_tasks.readlines():
            line = tasks.split(",")
            if len(line) > 2:
                print(f"""
                User: {line[0]}\n
                Task: {line[1]}\n
                Description: {line[2]}\n
                Assigned Date: {line[3]}\n
                Due Date: {line[4]}\n
                Task Complete: {line[-1]}
                """)


# View my tasks

def view_mine(valid=None):
    with open("tasks.txt", "r") as my_tasks:
        my_tasks = my_tasks.readlines()
        print(f"\nThe below tasks are all assigned to {username}:")

        for x, line in enumerate(my_tasks, 1):
            line = line.split(", ")
            if username == line[0]:
                print(f'''
                        Task number:\t\t {x}
                        Username:\t\t {line[0]}
                        Task:\t\t\t {line[1]}
                        Description:\t\t {line[2]}
                        Assigned date:\t\t {line[3]}
                        Due date:\t\t {line[4]}
                        Task complete:\t\t {line[-1]}
                        ''')

    with open("tasks.txt", "r+") as my_tasks:
        my_tasks = my_tasks.readlines()
        vm_select = int(input(
            "Type the task number you want to view or type '-1' to exit to the main menu: "))

        if (vm_select == -1) and (user_input == "admin, adm1n"):
            admin_menu()
        if (vm_select == -1) and (user_input in valid):
            normal_menu()

        for valid, lines in enumerate(my_tasks, 1):
            lines = lines.split(", ")
            if (vm_select == valid) and (username == lines[0]):
                print(f'''
                        Task number:\t\t {valid}
                        Username:\t\t {lines[0]}
                        Task:\t\t\t {lines[1]}
                        Description:\t\t {lines[2]}
                        Assigned date:\t\t {lines[3]}
                        Due date:\t\t {lines[4]}
                        Task complete:\t\t {lines[-1]}''')

                task_option = int(input('''
                                Task Options (select number):
                                1. Mark task as complete
                                2. Edit task
                                Selection: '''))

                # Mark Task as complete

                if task_option == 1:
                    sentences = ""
                    with open("tasks.txt", "r+") as complete:
                        for m, t in enumerate(complete, 1):
                            t = t.split(", ")
                            if m == valid:
                                t[5] = "Yes" + "\n"
                            sentences += ", ".join(t)
                        print(sentences)
                        with open("tasks.txt", "w") as complete:
                            complete.write(f"{sentences}")

                # Edit task

                elif task_option == 2:
                    edit_task = int(input('''
                                Edit Options (choose number):
                                1. Username
                                2. Due Date
                                Selection: '''))

                    # Username edit

                    if edit_task == 1:
                        edit_user = ""
                        with open("tasks.txt", "r+") as user_edit:
                            for u, e in enumerate(user_edit, 1):
                                e = e.split(", ")
                                if u == valid:
                                    e[0] = input("\nEnter new username here: ")
                                edit_user += ", ".join(e)
                            print(edit_user)
                            with open("tasks.txt", "w") as user_edit:
                                user_edit.write(f"{edit_user}")

                    # Date edit

                    elif edit_task == 2:
                        edit_date = ""
                        with open("tasks.txt", "r+") as date_edit:
                            for d, e in enumerate(date_edit, 1):
                                e = e.split(", ")
                                if d == valid:
                                    e[4] = input("\nEnter new due date here (eg. 5 Nov 2021): ")
                                edit_date += ", ".join(e)
                            print(edit_date)
                            with open("tasks.txt", "w") as date_edit:
                                date_edit.write(f"{edit_date}")

                    else:
                        print("You did not select a valid option.")

                else:
                    print("You did not select a valid option.")


# Generate report

def generate_report():
    from datetime import datetime
    with open("tasks.txt", "r") as generate_report:
        generate_report = generate_report.readlines()
        task_total = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        due_dates = 0
        overdue_tasks = 0
        incomplete_perc = 0
        overdue_perc = 0

        with open("task_overview.txt", "w") as task_overview:
            for gr in generate_report:
                gr = gr.strip("\n").split(", ")
                if len(gr) > 2:
                    due_dates = datetime.strptime(gr[3]
                                                  , "%d %b %Y")
                    task_total += 1

                    if gr[4] == "Yes":
                        completed_tasks += 1
                    else:
                        uncompleted_tasks += 1

                    if (datetime.today() > due_dates) and (gr[4] == "No"):
                        overdue_tasks += 1

                incomplete_perc = round((uncompleted_tasks / task_total) * 100, 2)
                overdue_perc = round((overdue_tasks / task_total) * 100, 2)

                task_overview.write(f'''Task Overview:
                            Task total:\t\t\t\t {task_total}
                            Completed Tasks:\t\t\t {completed_tasks}
                            Uncompleted Tasks:\t\t\t {uncompleted_tasks}
                            Overdue Tasks:\t\t\t\t {overdue_tasks}
                            Incomplete Task Percentage:\t\t {incomplete_perc}%
                            Overdue Task Percentage:\t\t {overdue_perc}%''')

            incomplete_perc = round((uncompleted_tasks / task_total) * 100, 2)
            overdue_perc = round((overdue_tasks / task_total) * 100, 2)

            task_overview.write(f'''Task Overview:
                        Task total:\t\t\t\t {task_total}
                        Completed Tasks:\t\t\t {completed_tasks}
                        Uncompleted Tasks:\t\t\t {uncompleted_tasks}
                        Overdue Tasks:\t\t\t\t {overdue_tasks}
                        Incomplete Task Percentage:\t\t {incomplete_perc}%
                        Overdue Task Percentage:\t\t {overdue_perc}%''')

            print(f'''
                Task Overview:
                Task total:\t\t\t\t {task_total}
                Completed Tasks:\t\t\t {completed_tasks}
                Uncompleted Tasks:\t\t\t {uncompleted_tasks}
                Overdue Tasks:\t\t\t\t {overdue_tasks}
                Incomplete Task Percentage:\t\t {incomplete_perc}%
                Overdue Task Percentage:\t\t {overdue_perc}%
                -------------------------------------------------------''')

    # Write to user overview txt file

    with open("user_overview.txt", "w") as user_overview:
        with open("user.txt", "r+") as user_report:
            user_report = user_report.readlines()
            with open("tasks.txt", "r+") as task_report:
                task_report = task_report.readlines()

                for ur in user_report:
                    ur = ur.split(", ")[0]
                    user_count = 0
                    task_count = 0
                    user_task_total = 0
                    user_task_perc = 0
                    task_comp = 0
                    task_incomp = 0
                    user_perc_complete = 0
                    user_perc_incomplete = 0
                    inc_overdue = 0
                    perc_inc_overdue = 0

                    user_count += 1

                    for tr in task_report:
                        tr = tr.strip("\n")
                        task_count += 1
                        if tr.startswith(ur):
                            if tr.endswith("Yes"):
                                task_comp += 1
                            if tr.endswith("No"):
                                task_incomp += 1
                            if (tr.endswith("No")) and (datetime.today() > due_dates):
                                inc_overdue += 1
                            user_task_total += 1

                    if user_task_total != 0:
                        user_task_perc = round((user_task_total / task_count) * 100, 2)
                    else:
                        user_task_perc = 0

                    if task_comp != 0:
                        user_perc_complete = round((task_comp / user_task_total) * 100, 2)
                    else:
                        user_perc_complete = 0

                    if task_incomp != 0:
                        user_perc_incomplete = round((task_incomp / user_task_total) * 100, 2)
                    else:
                        user_perc_incomplete = 0

                    if inc_overdue != 0:
                        perc_inc_overdue = (inc_overdue / user_task_total) * 100
                    else:
                        perc_inc_overdue = 0

                    user_overview.write(f'''
                                {ur} Report:
                                Total Tasks:\t\t\t\t {user_task_total}
                                Percentage Tasks assigned:\t\t {user_task_perc}%
                                Percentage completed:\t\t\t {user_perc_complete}%
                                Percentage incomplete:\t\t\t {user_perc_incomplete}%
                                Percentage incomplete and overdue:\t {perc_inc_overdue}%
                                ''')

                    print(f'''
                        {ur} Report:
                        Total Tasks:\t\t\t\t {user_task_total}
                        Percentage Tasks assigned:\t\t {user_task_perc}%
                        Percentage completed:\t\t\t {user_perc_complete}%
                        Percentage incomplete:\t\t\t {user_perc_incomplete}%
                        Percentage incomplete and overdue:\t {perc_inc_overdue}%
                        ''')


def insert_report():
    from datetime import datetime
    with open("tasks.txt", "r") as generate_report:
        generate_report = generate_report.readlines()
        task_total = 0
        completed_tasks = 0
        uncompleted_tasks = 0
        due_dates = 0
        overdue_tasks = 0
        incomplete_perc = 0
        overdue_perc = 0

        with open("task_overview.txt", "w") as task_overview:
            for gr in generate_report:
                gr = gr.strip("\n").split(", ")
                due_dates = datetime.strptime(gr[4], "%d %B ,%y")
                task_total += 1

                if gr[5] == "Yes":
                    completed_tasks += 1
                else:
                    uncompleted_tasks += 1

                if (datetime.today() > due_dates) and (gr[5] == "No"):
                    overdue_tasks += 1

            incomplete_perc = round((uncompleted_tasks / task_total) * 100, 2)
            overdue_perc = round((overdue_tasks / task_total) * 100, 2)

            task_overview.write(f'''Task Overview:
                        Task total:\t\t\t\t {task_total}
                        Completed Tasks:\t\t\t {completed_tasks}
                        Uncompleted Tasks:\t\t\t {uncompleted_tasks}
                        Overdue Tasks:\t\t\t\t {overdue_tasks}
                        Incomplete Task Percentage:\t\t {incomplete_perc}%
                        Overdue Task Percentage:\t\t {overdue_perc}%''')

        # user_overview

        with open("user_overview.txt", "w") as user_overview:
            with open("user.txt", "r+") as user_report:
                user_report = user_report.readlines()
                with open("tasks.txt", "r+") as task_report:
                    task_report = task_report.readlines()

                    for ur in user_report:
                        ur = ur.split(", ")[0]
                        user_count = 0
                        task_count = 0
                        user_task_total = 0
                        user_task_perc = 0
                        task_comp = 0
                        task_incomp = 0
                        user_perc_complete = 0
                        user_perc_incomplete = 0
                        inc_overdue = 0
                        perc_inc_overdue = 0

                        user_count += 1

                        for tr in task_report:
                            tr = tr.strip("\n")
                            task_count += 1
                            if tr.startswith(ur):
                                if tr.endswith("Yes"):
                                    task_comp += 1
                                if tr.endswith("No"):
                                    task_incomp += 1
                                if (tr.endswith("No")) and (datetime.today() > due_dates):
                                    inc_overdue += 1
                                user_task_total += 1

                        if user_task_total != 0:
                            user_task_perc = round((user_task_total / task_count) * 100, 2)
                        else:
                            user_task_perc = 0

                        if task_comp != 0:
                            user_perc_complete = round((task_comp / user_task_total) * 100, 2)
                        else:
                            user_perc_complete = 0

                        if task_incomp != 0:
                            user_perc_incomplete = round((task_incomp / user_task_total) * 100, 2)
                        else:
                            user_perc_incomplete = 0

                        if inc_overdue != 0:
                            perc_inc_overdue = (inc_overdue / user_task_total) * 100
                        else:
                            perc_inc_overdue = 0

                        user_overview.write(f'''
                                        {ur} Report:
                                        Total Tasks:\t\t\t\t {user_task_total}
                                        Percentage Tasks assigned:\t\t {user_task_perc}%
                                        Percentage completed:\t\t\t {user_perc_complete}%
                                        Percentage incomplete:\t\t\t {user_perc_incomplete}%
                                        Percentage incomplete and overdue:\t {perc_inc_overdue}%
                                        ''')


if menu_selection == "r":
    reg_user()

# Add task

if menu_selection == "a":
    add_task()

# View all tasks

if menu_selection == "va":
    view_all()

# View my tasks

if menu_selection == "vm":
    view_mine()

# Generate report

if menu_selection == "gr":
    generate_report()

# Statistics

if menu_selection == "s":
    insert_report()

    # User Stats

    user_stat_list = []
    user_stat_total = 0
    with open("user_overview.txt", "r") as user_stats:
        user_stats = user_stats.readlines()
        for us in user_stats:
            us = us.strip().split("\t ")
            user_stat_list.append(us)

        for ust in user_stat_list:
            if "Total Tasks:\t\t\t" in ust:
                user_stat_total += 1
        print(f"Users:\t\t\t {user_stat_total}")

    # Task stats

    task_stat_list = []
    task_stat_total = 0
    with open("task_overview.txt", "r") as task_stats:
        task_stats = task_stats.readlines()
        for ts in task_stats:
            ts = ts.strip().split("\t ")
            task_stat_list.append(ts)

        for tst in task_stat_list:
            if "Task total:\t\t\t" in tst:
                task_stat_total = tst[1]
    print(f"Tasks:\t\t\t {task_stat_total}")

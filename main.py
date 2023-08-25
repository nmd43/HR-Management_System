import tkinter
from datetime import datetime
import babel.numbers
import babel.dates
from tkcalendar import Calendar
import babel.numbers
import babel.dates
import secrets
import string
from PIL import ImageTk, Image
import functions

# used for editing in manager page
global edit_id

# used for knowing which employee has logged in
global employee_id

budgeting_id = 0

# creation of all GUI pages
login = tkinter.Tk()
login.configure(background="white")
login.attributes("-fullscreen", True)

manager = tkinter.Tk()
manager.configure(background="white")
manager.attributes("-fullscreen", True)
manager.withdraw()

employee = tkinter.Tk()
employee.configure(background="white")
employee.attributes("-fullscreen", True)
employee.withdraw()

add = tkinter.Tk()
add.configure(background="white")
add.attributes("-fullscreen", True)
add.withdraw()

values = tkinter.Tk()
values.configure(background="white")
values.attributes("-fullscreen", True)
values.withdraw()

cal_tk = tkinter.Tk()
cal_tk.configure(background="white")
cal_tk.attributes("-fullscreen", True)
cal_tk.withdraw()

edit = tkinter.Tk()
edit.configure(background="white")
edit.attributes("-fullscreen", True)
edit.withdraw()

created_password_page = tkinter.Tk()
created_password_page.configure(background="white")
created_password_page.geometry("400x200")
created_password_page.eval('tk::PlaceWindow . center')
created_password_page.withdraw()

new_password = tkinter.Tk()
new_password.configure(background="white")
new_password.attributes("-fullscreen", True)
new_password.withdraw()

budget = tkinter.Tk()
budget.configure(background="white")
budget.attributes("-fullscreen", True)
budget.withdraw()

add_budget = tkinter.Tk()
add_budget.configure(background="white")
add_budget.attributes("-fullscreen", True)
add_budget.withdraw()

update_budget = tkinter.Tk()
update_budget.configure(background="white")
update_budget.attributes("-fullscreen", True)
update_budget.withdraw()

extra_costs = tkinter.Tk()
extra_costs.configure(background="white")
extra_costs.attributes("-fullscreen", True)
extra_costs.withdraw()

budget_calculations = tkinter.Tk()
budget_calculations.configure(background="white")
budget_calculations.attributes("-fullscreen", True)
budget_calculations.withdraw()

feedback = tkinter.Tk()
feedback.configure(background="white")
feedback.attributes("-fullscreen", True)
feedback.withdraw()

feedback_display = tkinter.Tk()
feedback_display.configure(background="white")
feedback_display.attributes("-fullscreen", True)
feedback_display.withdraw()

search = tkinter.Tk()
search.configure(background="white")
width = search.winfo_screenwidth()
search.geometry("%dx280+0+220" % width)
search.withdraw()

show_leaves = tkinter.Tk()
show_leaves.configure(background="white")
show_leaves.attributes("-fullscreen", True)
show_leaves.withdraw()

confirmation = tkinter.Tk()
confirmation.configure(background="white")
confirmation.geometry("600x300+500+250")
confirmation.withdraw()


# function to end GUI using 'X' button
def del_gui():
    functions.end()
    add.destroy()
    values.destroy()
    cal_tk.destroy()
    edit.destroy()
    employee.destroy()
    manager.destroy()
    login.destroy()
    created_password_page.destroy()
    new_password.destroy()
    budget.destroy()
    add_budget.destroy()
    update_budget.destroy()
    extra_costs.destroy()
    budget_calculations.destroy()
    search.destroy()
    feedback.destroy()
    feedback_display.destroy()
    show_leaves.destroy()
    confirmation.destroy()


# functions for showing each page
def show_login():
    employee.withdraw()
    manager.withdraw()
    login.deiconify()


def show_cal():
    cal_tk.deiconify()
    employee.withdraw()


def show_add():
    add.deiconify()
    manager.withdraw()


def show_edit():
    edit.deiconify()
    values.withdraw()


def show_employee():
    cal_tk.withdraw()
    employee.deiconify()
    login.withdraw()
    new_password.withdraw()


def show_manager():
    edit.withdraw()
    add.withdraw()
    values.withdraw()
    manager.deiconify()
    show_leaves.withdraw()
    login.withdraw()
    feedback_display.withdraw()


def show_values():
    edit.withdraw()
    values.deiconify()


def show_budget():
    manager.withdraw()
    add_budget.withdraw()
    update_budget.withdraw()
    extra_costs.withdraw()
    budget_calculations.withdraw()
    budget.deiconify()


def show_password():
    employee.withdraw()
    new_password.deiconify()


def show_add_budget():
    add_budget.deiconify()
    update_budget.withdraw()
    extra_costs.withdraw()
    budget_calculations.withdraw()
    budget.withdraw()


def show_update_budget():
    add_budget.withdraw()
    update_budget.deiconify()
    extra_costs.withdraw()
    budget_calculations.withdraw()
    budget.withdraw()


def show_extra_costs():
    add_budget.withdraw()
    update_budget.withdraw()
    extra_costs.deiconify()
    budget_calculations.withdraw()
    budget.withdraw()


def show_feedback():
    employee.withdraw()
    feedback.deiconify()


def show_feedback_display():
    manager.withdraw()
    feedback_display.deiconify()


def show_confirm():
    confirmation.deiconify()


# delete all widgets in created_password_page
def clear_value_display():
    for widget in created_password_page.winfo_children():
        widget.destroy()
    created_password_page.withdraw()


# removing the error message for add_employee values
def delete_unfilled_add(e):
    unfilled_add.grid_forget()


# removing the error message for incorrect login credentials
def del_incorrect_login(e):
    incorrect_login.grid_forget()


# removing the error message on budget page
def del_wrong_budget(e):
    budget_wrong_id.grid_forget()


# changing the password of an employee
def create_password():
    original = og_password.get()
    new = created_password.get()
    if len(original) != 0 or len(new) != 0:
        # creates an instance of IdFunctions class
        pass_changer = functions.IdFunctions(edit_id)
        returned = pass_changer.change_password(original=original, new_password=new)
        # Checks whether original password entered is correct
        if not returned:
            tkinter.Label(new_password, text="Incorrect Original Password", bg='white',
                          font=("Franklin Gothic Book", 20), fg='red').grid(row=5, column=2)
        else:
            for widget in new_password.winfo_children():
                if isinstance(widget, tkinter.Entry):
                    widget.delete(0, tkinter.END)
            show_employee()


# reading employee values from the user input
def add_val():
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    month_dob = sel_month_dob.get()
    day_dob = sel_day_dob.get()
    year_dob = sel_year_dob.get()
    month_doj = sel_month_doj.get()
    day_doj = sel_day_doj.get()
    year_doj = sel_year_doj.get()
    text4 = f"{day_dob}-{month_dob}-{year_dob}"
    text5 = f"{day_doj}-{month_doj}-{year_doj}"
    text6 = sel_sex.get()

    # reads name and removes spaces to create username
    text7 = entry1.get().replace(" ", "").casefold()
    # creates a randomized password
    alphabet = string.ascii_letters + string.digits
    text8 = ''.join(secrets.choice(alphabet) for _ in range(6))
    if not text1.replace(' ', '').isalpha() or not text2.isdigit() or len(text3) == 0:
        unfilled_add.grid(row=7, column=2)

    else:

        functions.add_value([text1, text2, text3, text4, text5, text6, text7, text8])
        # GUI for displaying the username and password of an added employee
        created_password_page.deiconify()
        tkinter.Label(created_password_page, text="", bg="white").grid(row=0, column=0)
        tkinter.Label(created_password_page, text="Username", bg="white").grid(row=1, column=1)
        data_string = tkinter.StringVar(created_password_page)
        data_string.set(text7)
        tkinter.Entry(created_password_page, textvariable=data_string, bg="white", bd=0, state="readonly").grid(row=1, column=2)
        tkinter.Label(created_password_page, text="", bg="white").grid(row=2)
        tkinter.Label(created_password_page, text="Password", bg="white").grid(row=3, column=1)
        data_string = tkinter.StringVar(created_password_page)
        data_string.set(text8)
        tkinter.Entry(created_password_page, textvariable=data_string, bg="white", bd=0, state="readonly").grid(row=3, column=2)
        tkinter.Label(created_password_page, text="", bg="white").grid(row=4)
        tkinter.Label(created_password_page, text="You will never be able to see this page again", bg="white").grid(row=5, column=2)
        tkinter.Button(created_password_page, text="End Interaction", command=clear_value_display).grid(row=6, column=2)

    # resets all the entered values on GUI for adding a new employee
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    sel_month_dob.set("Jan")
    sel_day_dob.set("1")
    sel_year_dob.set("1970")
    sel_month_doj.set("Feb")
    sel_day_doj.set("11")
    sel_year_doj.set("2022")


# reads login credentials and checks whether they are correct
def login_user():
    user = str(username.get())
    code = str(password.get())
    # calls function that compares with correct credentials
    request_id = functions.login_check(user, code)
    if request_id == 0:
        incorrect_login.grid(row=4, column=2)
        username.delete(0, tkinter.END)
        password.delete(0, tkinter.END)

    # directs to manager page
    elif request_id == 1:
        show_manager()
    # directs to employee page
    else:
        global edit_id
        edit_id = request_id
        show_employee()

    # clears the user input on login page for next user
    for widget in login.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, tkinter.END)


# creates the view all employees page
def show_all():
    confirmation.withdraw()
    # empties all cells in the show employees table
    for widget in values.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, "end")

    # search employee page construction
    def searcher():
        for entry in search.winfo_children():
            entry.destroy()
        if search_value.get() is None:
            pass
        else:
            search.overrideredirect(True)
            search.deiconify()
            tkinter.Label(search, text='', width=22, bg="white").grid(column=0)

            # calls the linear search algorithm
            returned = functions.searcher(search_value.get())
            # gets all employee details for the matching value as search
            required_people = functions.read_ids(returned)
            # creating the table of searched employees
            for a in range(len(required_people)):
                for b in range(7):
                    if b == 0 or b == 6:
                        employee_entry = tkinter.Entry(search, font=("Franklin Gothic Book", 15),
                                                       borderwidth=1, relief="solid", width=10,
                                                       justify='center')
                        employee_entry.insert(0, required_people[a][b])
                    elif b == 1:
                        employee_entry = tkinter.Entry(search, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=19,
                                                       justify='center')
                        employee_entry.insert(0, required_people[a][b])
                    elif b == 3:
                        employee_entry = tkinter.Entry(search, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=17,
                                                       justify='center')
                        employee_entry.insert(0, required_people[a][b])
                    else:
                        employee_entry = tkinter.Entry(search, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=14,
                                                       justify='center')
                        employee_entry.insert(0, required_people[a][b])

                    employee_entry.grid(row=a, column=b+1)

    manager.withdraw()
    edit.withdraw()
    values.deiconify()
    people = functions.employees()
    total_people = len(people)

    # checks if there are any employees in the database
    if total_people > 1:
        # creating the GUI widgets for the search function
        tkinter.Label(values, text="Search", font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=1, column=1)
        search_value = tkinter.Entry(values, font=("Franklin Gothic Book", 15), width=10)
        search_value.grid(row=1, column=2)
        tkinter.Button(values, text="Search", font=("Franklin Gothic Book", 15, "bold"), command=searcher, bg="#6cb444", fg="white").grid(row=1, column=3)
        tkinter.Label(values, text="Employee ID", font=("Franklin Gothic Book", 15), width=11, bg="#6cb444").grid(row=2, column=0, sticky="w", padx=(166, 0))
        tkinter.Label(values, text="Full Name", font=("Franklin Gothic Book", 15), width=21, bg="#6cb444").grid(row=2, column=0, sticky="e", padx=(0, 4))
        tkinter.Label(values, text="Contact No.", font=("Franklin Gothic Book", 15), width=15, bg="#6cb444").grid(row=2, column=1)
        tkinter.Label(values, text="Email ID", font=("Franklin Gothic Book", 15), width=17, bg="#6cb444").grid(row=2, column=2)
        tkinter.Label(values, text="Date of Birth", font=("Franklin Gothic Book", 15), width=15, bg="#6cb444").grid(row=2, column=3)
        tkinter.Label(values, text="Date of Joining", font=("Franklin Gothic Book", 15), width=15, bg="#6cb444").grid(row=2, column=4)
        tkinter.Label(values, text="Gender", font=("Franklin Gothic Book", 15), width=11, bg="#6cb444").grid(row=2, column=5)

        # creating the show employees table with all employees
        for i in range(total_people-1):
            for j in range(7):
                if j == 0:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=10,
                                           justify='center')
                    button.insert(0, people[i+1][j])
                    button.grid(row=i+3, column=j, sticky="w", padx=(161, 0))
                elif j == 6:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=10,
                                           justify='center')
                    button.insert(0, people[i+1][j])
                    button.grid(row=i+3, column=j-1)
                elif j == 1:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=19,
                                           justify='center')
                    button.insert(0, people[i + 1][j])
                    button.grid(row=i+3, column=j-1, sticky='e')
                elif j == 3:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=17,
                                           justify='center')
                    button.insert(0, people[i + 1][j])
                    button.grid(row=i+3, column=j-1)
                else:
                    button = tkinter.Entry(values, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=14,
                                           justify='center')
                    button.insert(0, people[i + 1][j])
                    button.grid(row=i+3, column=j-1)

    # message if there are no employees to be displayed
    else:
        empty_label.grid(row=1, column=1)

    for c in range(total_people+3, 11):
        tkinter.Label(values, text="", bg="white").grid(row=c)


def delete_confirm():
    confirmation.withdraw()
    delete_value()


# delete employee from database when requested by user
def delete_value():
    deleter = functions.IdFunctions(delete_entry.get())
    deleter.deleting_value()
    show_all()


# creates the edit employee GUI
def edit_value():
    show_edit()
    for widget in edit.winfo_children():
        if isinstance(widget, tkinter.Entry):
            widget.delete(0, tkinter.END)
    for widget in edit_doj_frame.winfo_children():
        widget.destroy()
    for widget in edit_dob_frame.winfo_children():
        widget.destroy()

    editer = functions.IdFunctions(edit_entry.get())
    collected_values = editer.collect_employee_details()
    # sets values for DOB dropdown menus
    edited_day_dob.set(collected_values[3])
    edited_month_dob.set(collected_values[4])
    edited_year_dob.set(collected_values[5])
    name.insert(tkinter.END, collected_values[0])
    phone.insert(tkinter.END, collected_values[1])
    email.insert(tkinter.END, collected_values[2])
    tkinter.OptionMenu(edit_dob_frame, edited_month_dob, *months).pack(side=tkinter.LEFT)
    tkinter.OptionMenu(edit_dob_frame, edited_day_dob, *days).pack(side=tkinter.LEFT, padx=64)
    tkinter.OptionMenu(edit_dob_frame, edited_year_dob, *dob_years).pack(side=tkinter.LEFT)
    # sets values for DOJ dropdown menus
    edited_day_doj.set(collected_values[6])
    edited_month_doj.set(collected_values[7])
    edited_year_doj.set(collected_values[8])
    tkinter.OptionMenu(edit_doj_frame, edited_month_doj, *months).pack(side=tkinter.LEFT)
    tkinter.OptionMenu(edit_doj_frame, edited_day_doj, *days).pack(side=tkinter.LEFT, padx=64)
    tkinter.OptionMenu(edit_doj_frame, edited_year_doj, *doj_years).pack(side=tkinter.LEFT)
    edited_sex.set(collected_values[9])
    edit.deiconify()


# reads edited employee values from user and updates the database
def edit_button():
    editer = functions.IdFunctions(edit_entry.get())
    edited_name = name.get()
    edited_phone = phone.get()
    edited_email = email.get()
    edited_dob = f"{edited_day_dob.get()}-{edited_month_dob.get()}-{edited_year_dob.get()}"
    edited_doj = f"{edited_day_doj.get()}-{edited_month_doj.get()}-{edited_year_doj.get()}"
    edit_sex = edited_sex.get()
    data = edited_name, edited_phone, edited_email, edited_dob, edited_doj, edit_sex
    editer.edit_button(data)
    show_all()
    edit.withdraw()
    values.deiconify()


# reads value from calendar and adds the leaves to the database
# displays the total leaves selected
def total_leave():
    tkinter.Label(cal_tk, text="Total Leave: ", bg="white", font=("Franklin Gothic Book", 15)).grid(row=10, column=1)
    date_format = "%m/%d/%y"
    a = datetime.strptime(cal1.get_date(), date_format)
    b = datetime.strptime(cal2.get_date(), date_format)
    start = str(a)
    end = str(b)
    delta = (b - a)
    tkinter.Label(cal_tk, text=delta.days, bg="white", font=("Franklin Gothic Book", 15)).grid(row=10, column=2)
    leaver = functions.IdFunctions(edit_id)
    # check if the employee has previously recoded available leaves
    if leaver.select_available_leave() is not None:
        available = leaver.select_available_leave()
    else:
        available = 30

    print(f"Available from main: {available}, {delta.days}")
    leaver.insert_leave(delta.days, available - delta.days, start, end)


# Allows the manager to view leaves entered by the employees
def create_show_leave():
    show_leaves.deiconify()
    manager.withdraw()
    for value in show_leaves.winfo_children():
        if isinstance(value, tkinter.Entry):
            value.delete(0, tkinter.END)
    tkinter.Label(show_leaves, text="Employee ID", font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=2, column=1)
    tkinter.Label(show_leaves, text="Leaves", font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=2, column=2)
    tkinter.Label(show_leaves, text="Start Date", font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=2, column=4)
    tkinter.Label(show_leaves, text="End Date", font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=2, column=5)
    tkinter.Label(show_leaves, text="Available Leaves", font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=2, column=3)

    # creation of a table to display leaves to manager portal
    all_leaves = functions.read_leaves()
    for i in range(len(all_leaves)):
        for j in range(5):
            leave = tkinter.Entry(show_leaves, font=("Franklin Gothic Book", 15),
                                  borderwidth=1, relief="solid", width=15)
            leave.grid(row=i + 3, column=j+1)
            leave.insert(0, all_leaves[i][j])


# writing or updating the total budget
def update_total_budget():
    write = open("total_budget.txt", "w")
    write.write(total_budget.get())
    write.close()


# adds an employee into budget table with salary
def employee_add_budget():
    result = functions.add_budget(add_budget_id.get(), add_budget_quantity.get())
    if result == 0:
        budget_wrong_id.grid(row=3, column=3)

    add_budget_id.delete(0, tkinter.END)
    add_budget_quantity.delete(0, tkinter.END)


# adds first extra cost for existing employee
def add_extra_costs():
    returned = functions.add_extra_costs(extra_cost_id.get(), int(extra_costs_value.get()), extra_cost_type.get())
    if returned == 0:
        used_cost_id = tkinter.Label(extra_costs, text="This ID has been used", font=('Franklin Gothic Book', 15), fg="red", bg="white")
        used_cost_id.grid(row=3, column=5)
    elif returned == 1:
        extra_cost_id.delete(0, tkinter.END)
        extra_costs_value.delete(0, tkinter.END)
        extra_cost_type.delete(0, tkinter.END)


# updates employee salary and extra costs once already added
def employee_update_budget():
    functions.edit_employee(update_budget_id.get(), update_budget_quantity.get(), update_extra_cost.get(),
                            update_cost_type.get())
    update_budget_id.delete(0, tkinter.END)
    update_budget_quantity.delete(0, tkinter.END)
    update_extra_cost.delete(0, tkinter.END)
    update_cost_type.delete(0, tkinter.END)


# prefills existing values on the update salary and extra costs page
def budget_update_setup():
    unorganized_edit = functions.get_edit_values(update_budget_id.get())
    update_budget_quantity.delete(0, tkinter.END)
    update_budget_quantity.insert(0, unorganized_edit[1])
    update_extra_cost.delete(0, tkinter.END)
    update_extra_cost.insert(0, unorganized_edit[2])
    update_cost_type.delete(0, tkinter.END)
    if unorganized_edit[3] is not None:
        update_cost_type.insert(0, unorganized_edit[3])


# GUI for showing each employee, their salary, and extra costs
def budget_show_all():
    budget.withdraw()
    budget_calculations.deiconify()
    read_values = functions.organized_budget()
    all_budget_values = read_values[0]
    length_of_budget = read_values[1]
    for o in budget_calculations.winfo_children():
        if isinstance(o, tkinter.Canvas) is False:
            o.destroy()
    tkinter.Button(budget_calculations, text="Back", command=show_budget, height=2, width=7, bg="dark gray").grid(column=6, row=0, sticky="n", padx=10, pady=4)
    if length_of_budget != 0:
        tkinter.Label(budget_calculations, text="Employee ID", font=("Franklin Gothic Book", 15), bg="white", fg="green").grid(row=2, column=1)
        tkinter.Label(budget_calculations, text="Salary", font=("Franklin Gothic Book", 15), bg="white", fg="green").grid(row=2, column=2)
        tkinter.Label(budget_calculations, text="Extra Costs", font=("Franklin Gothic Book", 15), bg="white", fg="green").grid(row=2, column=3)
        tkinter.Label(budget_calculations, text="Cost Type", font=("Franklin Gothic Book", 15), bg="white", fg="green").grid(row=2, column=4)
        for i in range(length_of_budget):
            for j in range(4):
                p = tkinter.Entry(budget_calculations, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=15)
                p.grid(row=i + 3, column=j+1)
                if all_budget_values[i][j] is not None:
                    p.insert(0, all_budget_values[i][j])

        build_budget_calc(1)

    else:
        tkinter.Label(budget_calculations, text="No Added Employees",
                      font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=2, column=1)

        build_budget_calc(0)


# GUI for the budget calculation page
def build_budget_calc(empty):
    total_budget_people = functions.organized_budget()[1] + 3
    if empty == 1:
        tkinter.Label(budget_calculations, text="", bg="white").grid(row=total_budget_people)
        tkinter.Label(budget_calculations, text="Total Budget: ", font=("Franklin Gothic Book", 15), bg="white", fg="green")\
            .grid(row=total_budget_people+1, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[0], font=("Franklin Gothic Book", 15), borderwidth=1,
                      relief="solid", background='white').grid(row=total_budget_people+1, column=2)
        tkinter.Label(budget_calculations, text="", bg="white").grid(row=total_budget_people+2)
        tkinter.Label(budget_calculations, text="Used Budget: ", font=("Franklin Gothic Book", 15), fg="green", bg="white")\
            .grid(row=total_budget_people+3, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[1], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+3, column=2)
        tkinter.Label(budget_calculations, text="", bg="white").grid(row=total_budget_people+4)
        tkinter.Label(budget_calculations, text="Available Budget: ", font=("Franklin Gothic Book", 15), bg="white", fg="green") \
            .grid(row=total_budget_people+5, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[2], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+5, column=2)
        tkinter.Label(budget_calculations, text="", bg="white").grid(row=total_budget_people+6)
        tkinter.Label(budget_calculations, text="Salaries: ", font=("Franklin Gothic Book", 15), bg="white", fg="green") \
            .grid(row=total_budget_people+2, column=3)
        tkinter.Label(budget_calculations, text=functions.available_budget()[3], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+2, column=4)
        tkinter.Label(budget_calculations, text="Extra Costs: ", font=("Franklin Gothic Book", 15), bg="white", fg="green") \
            .grid(row=total_budget_people+4, column=3)
        tkinter.Label(budget_calculations, text=functions.available_budget()[4], font=("Franklin Gothic Book", 15),
                      borderwidth=1, relief="solid", background='white').grid(row=total_budget_people+4, column=4)
        tkinter.Button(budget_calculations, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=7, sticky="n", pady=4)
    else:
        tkinter.Label(budget_calculations, text="Total Budget: ", font=("Franklin Gothic Book", 15), bg="white", fg="green") \
            .grid(row=1, column=1)
        tkinter.Label(budget_calculations, text=functions.available_budget()[0], font=("Franklin Gothic Book", 15), borderwidth=1,
                      relief="solid", background='white').grid(row=1, column=2)
        tkinter.Label(budget_calculations, text="", bg="white").grid(row=2)


# GUI to create the Read Feedback page
def create_feedback():
    feedback_display.deiconify()
    manager.withdraw()
    read_feedback = functions.read_feedback()

    for widget in feedback_display.winfo_children():
        widget.destroy()
    feedback_display_canvas = tkinter.Canvas(feedback_display, width=350, height=150, highlightthickness=0, bg="white")
    feedback_display_canvas.grid(row=0, column=0, sticky="w")
    feedback_display_img = (Image.open("placeholder.jpg"))
    feedback_display_new_image = ImageTk.PhotoImage(master=feedback_display_canvas, image=feedback_display_img)
    feedback_display_canvas.create_image(40, 30, anchor="nw", image=feedback_display_new_image)
    frame = tkinter.Frame(feedback_display, bg="white")
    frame.grid(row=1, column=0)
    # creating scroll bar and textbox for feedback
    s = tkinter.Scrollbar(frame, troughcolor='red')
    s.pack(side=tkinter.RIGHT, fill=tkinter.Y, padx=(0, 20), pady=20)
    t = tkinter.Text(frame, height=15, wrap=tkinter.WORD,
                     yscrollcommand=s.set, font=("Franklin Gothic Book", 22))
    t.pack(side=tkinter.TOP, fill=tkinter.X, pady=20, padx=(20, 0))
    # configuring the scrollbar onto the textbox
    s.config(command=t.yview)

    # inserting feedback in the textbox
    for o in read_feedback:
        t.insert(tkinter.END, str(o[1]) + "\n\n")

    back = tkinter.Button(frame, text="Back", bg="#6cb444", fg="white", command=show_manager, font=("Franklin Gothic Book", 15))
    back.pack(side=tkinter.BOTTOM)
    back = tkinter.Button(feedback_display)
    back.pack(side=tkinter.BOTTOM)


# Reads feedback from the database and displays on feedback page
def display_feedback():
    all_feedback = functions.read_feedback()
    if len(all_feedback) == 0:
        tkinter.Label(feedback_display, text="", width=40, height=2, bg="white").grid(row=0, column=0)
        tkinter.Label(feedback_display, text="You have no feedback!",
                      font=("Franklin Gothic Book", 15), bg="white", fg="#6cb444").grid(row=1, column=1)
    for i in range(len(all_feedback)):
        tkinter.Label(feedback_display, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid", width=15,
                      text=all_feedback[i][1]).grid(row=i + 3, column=1)


# Reads employee feedback and stores in the database
def submit_feedback():
    functions.send_feedback(typed_feedback.get())
    typed_feedback.delete(0, tkinter.END)
    feedback.withdraw()
    employee.deiconify()


# Creating login page GUI
canvas = tkinter.Canvas(login, width=350, height=150, highlightthickness=0, bg="white")
canvas.grid(row=0, column=0)
img = (Image.open("placeholder.jpg"))
new_image = ImageTk.PhotoImage(master=canvas, image=img)
canvas.create_image(40, 30, anchor="nw", image=new_image)
tkinter.Label(login, text="Login Page", height=3, bg="white", font=("Franklin Gothic Book", 35, "bold"), fg="#6cb444")\
    .grid(row=1, column=2)
tkinter.Label(login, text="Username: ", font=("Franklin Gothic Book", 20),
              height=2, bg="white", width=18).grid(row=2, column=1)
username = tkinter.Entry(login, font=("Franklin Gothic Book", 20), bg="white", borderwidth=2, relief="solid")
username.grid(row=2, column=2)
username.bind("<FocusIn>", del_incorrect_login)
tkinter.Label(login, text="Password: ", font=("Franklin Gothic Book", 20), height=2, bg="white").grid(row=3, column=1)
password = tkinter.Entry(login, show="*", font=("Franklin Gothic Book", 20), bg="white", borderwidth=2, relief="solid")
password.grid(row=3, column=2)
tkinter.Label(login, text="", width=74, bg="white").grid(column=3)
incorrect_login = tkinter.Label(login, text="Incorrect Credentials", font=("Franklin Gothic Book", 15),
                                fg="red", borderwidth=0, highlightthickness=0, bg="white")
incorrect_login.grid(row=4, column=2)
incorrect_login.grid_forget()
tkinter.Button(login, text="Login", command=login_user, font=("Franklin Gothic Book", 20), relief="ridge", borderwidth=2,
               bg="#6cb444", fg="white").grid(row=5, column=2)
tkinter.Button(login, text="X", width=7, height=2, command=del_gui, bg="red").grid(row=0, column=4, sticky="ne", padx=10, pady=4)


# Creating the welcome employee page GUI
employee_canvas = tkinter.Canvas(employee, width=350, height=150, highlightthickness=0, bg="white")
employee_canvas.grid(row=0, column=0, sticky="w")
employee_img = (Image.open("placeholder.jpg"))
employee_new_image = ImageTk.PhotoImage(master=employee_canvas, image=employee_img)
employee_canvas.create_image(40, 30, anchor="nw", image=employee_new_image)

tkinter.Label(employee, text="", width=45, bg="white").grid(column=1)
tkinter.Label(employee, text="Welcome Employee!", bg="white", fg="#6cb444", font=("Franklin Gothic Book", 30)).grid(row=1, column=2)
tkinter.Label(employee, text="", bg="white", height=2).grid(row=2)
tkinter.Button(employee, text="Apply For Leave", font=("Franklin Gothic Book", 20), command=show_cal, bg="#6cb444", width=17).grid(column=2, row=3)
tkinter.Label(employee, text="", height=2, bg="white").grid(row=4, column=0)
tkinter.Button(employee, text="Raise Feedback", font=("Franklin Gothic Book", 20), command=show_feedback, bg="#6cb444", width=17).grid(column=2, row=5)
tkinter.Label(employee, text="", height=2, bg="white").grid(row=6, column=0)
tkinter.Button(employee, text="Change Password", font=("Franklin Gothic Book", 20), command=show_password, bg="#6cb444", width=17).grid(column=2, row=7)
tkinter.Label(employee, text="", bg="white", width=51).grid(column=3)
tkinter.Button(employee, text="Back", command=show_login, height=2, width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(employee, text="X", command=del_gui, width=7, height=2, bg="red").grid(column=5, row=0, sticky="n", pady=4)

# Creating manager page GUI
tkinter.Label(manager, text="", width=30, bg="white").grid(row=1, column=0)
manager_canvas = tkinter.Canvas(manager, width=350, height=150, highlightthickness=0, bg="white")
manager_canvas.grid(row=0, column=0, sticky="w")
manager_img = (Image.open("placeholder.jpg"))
manager_new_image = ImageTk.PhotoImage(master=manager_canvas, image=manager_img)
manager_canvas.create_image(40, 30, anchor="nw", image=manager_new_image)

tkinter.Button(manager, text="Add Employee", command=show_add, bg="#6cb444", fg="white", font=("Franklin Gothic Book", 20), width=20)\
    .grid(column=1, row=2)
tkinter.Label(manager, text="Manager Page", height=5, fg="#6cb444", bg="white", font=("Franklin Gothic Book", 25, "bold")).grid(row=1, column=2, padx=20)
tkinter.Button(manager, text="Show Employees", font=("Franklin Gothic Book", 20), command=show_all, bg="#6cb444", fg="white", width=20)\
    .grid(column=3, row=2)
tkinter.Label(manager, text="", bg='white', height=2).grid(row=3)
tkinter.Button(manager, text="Budget Management", command=show_budget, font=("Franklin Gothic Book", 20), bg="#6cb444", fg="white", width=20)\
    .grid(column=1, row=4)
tkinter.Button(manager, text="Read Feedback", font=("Franklin Gothic Book", 20), command=create_feedback, bg="#6cb444", fg="white", width=20)\
    .grid(row=4, column=3)
tkinter.Label(manager, text="").grid(row=5)
tkinter.Button(manager, text="View Leaves", font=("Franklin Gothic Book", 20), command=create_show_leave, bg="#6cb444", fg="white", width=20).grid(row=6, column=2)
tkinter.Label(manager, text="", bg="white", width=23).grid(column=4)
tkinter.Button(manager, text="Back", command=show_login, height=2, width=7, bg="dark gray").grid(column=5, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(manager, text="X", command=del_gui, width=7, height=2, bg="red").grid(column=6, row=0, sticky="n", pady=4)

# Creating add employees GUI
tkinter.Label(add, text="", width=75, height=2, bg="white").grid(row=0, column=0)
tkinter.Label(add, text="", width=49, bg="white").grid(row=0, column=3)
add_canvas = tkinter.Canvas(add, width=350, height=150, highlightthickness=0, bg="white")
add_canvas.grid(row=0, column=0, sticky="w")
add_img = (Image.open("placeholder.jpg"))
add_new_image = ImageTk.PhotoImage(master=add_canvas, image=add_img)
add_canvas.create_image(40, 30, anchor="nw", image=add_new_image)
tkinter.Label(add, text="Full Name: ", width=10, font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=1, column=1)
entry1 = tkinter.Entry(add, width=20, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
entry1.grid(row=1, column=2)
entry1.bind("<FocusIn>", delete_unfilled_add)
tkinter.Label(add, text="Contact No.: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=2, column=1)
entry2 = tkinter.Entry(add, width=20, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
entry2.grid(row=2, column=2)
tkinter.Label(add, text="Email ID: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=3, column=1)
entry3 = tkinter.Entry(add, width=20, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
entry3.grid(row=3, column=2)
tkinter.Label(add, text="Date of Birth: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=4, column=1)
frame1 = tkinter.Frame(add, bg="white")
frame1.grid(row=4, column=2, sticky="nsew")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sel_month_dob = tkinter.StringVar(frame1)
sel_month_dob.set("Jan")
days = [x for x in range(1, 32)]
sel_day_dob = tkinter.StringVar(frame1)
sel_day_dob.set('1')
dob_years = [x for x in range(1960, 2005)]
sel_year_dob = tkinter.StringVar(frame1)
sel_year_dob.set('1960')
month_entry_dob = tkinter.OptionMenu(frame1, sel_month_dob, *months)
month_entry_dob.pack(side=tkinter.LEFT)
day_entry_dob = tkinter.OptionMenu(frame1, sel_day_dob, *days)
day_entry_dob.pack(side=tkinter.LEFT, padx=64)
year_entry_dob = tkinter.OptionMenu(frame1, sel_year_dob, *dob_years)
year_entry_dob.pack(side=tkinter.LEFT)
tkinter.Label(add, text="Date of Joining: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=5, column=1)

frame2 = tkinter.Frame(add, bg="white")
frame2.grid(row=5, column=2, sticky="nsew")
doj_years = [x for x in range(2015, 2022)]
sel_month_doj = tkinter.StringVar(frame2)
sel_month_doj.set("Jan")
sel_day_doj = tkinter.StringVar(frame1)
sel_day_doj.set('1')
sel_year_doj = tkinter.StringVar(frame1)
sel_year_doj.set('2015')
month_entry_doj = tkinter.OptionMenu(frame2, sel_month_doj, *months)
month_entry_doj.pack(side=tkinter.LEFT)
day_entry_doj = tkinter.OptionMenu(frame2, sel_day_doj, *days)
day_entry_doj.pack(side=tkinter.LEFT, padx=64)
year_entry_doj = tkinter.OptionMenu(frame2, sel_year_doj, *doj_years)
year_entry_doj.pack(side=tkinter.LEFT)
tkinter.Label(add, text="Gender: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=6, column=1)
options = ["Male", "Female", "Others"]
sel_sex = tkinter.StringVar(add)
sel_sex.set("Male")
entry6 = tkinter.OptionMenu(add, sel_sex, *options)
entry6.grid(row=6, column=2)
unfilled_add = tkinter.Label(add, text="Fill All Fields", fg="red", font=("Franklin Gothic Book", 20), bg="white")
unfilled_add.grid(row=7, column=2)
unfilled_add.grid_forget()
tkinter.Button(add, text="Enter", command=add_val, font=("Franklin Gothic Book", 20), bg="#6cb444", fg="white").grid(column=2, row=8)
tkinter.Button(add, text="Back", command=show_manager, height=2, width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(add, text="X", bg="red", command=del_gui, width=7, height=2).grid(column=5, row=0, sticky="n", pady=4)


# Creating Show Employees GUI
for i in range(20):
    tkinter.Label(values, text="", bg="white").grid(row=i)

people = functions.employees()

tkinter.Label(values, text="", bg="white", width=73).grid(row=0, column=0)
values_canvas = tkinter.Canvas(values, width=350, height=150, highlightthickness=0, bg="white")
values_canvas.grid(row=0, column=0, sticky="w")
values_img = (Image.open("placeholder.jpg"))
values_new_image = ImageTk.PhotoImage(master=values_canvas, image=values_img)
values_canvas.create_image(40, 30, anchor="nw", image=values_new_image)
empty_label = tkinter.Label(values, text="This database is currently empty. Go back to add an employee.", font=("Franklin Gothic Book", 15), bg="white")
empty_label.grid(row=1, column=1)
empty_label.grid_forget()
tkinter.Button(values, text="Show All", command=show_all, font=("Franklin Gothic Book", 12), fg="white", bg="#6cb444").grid(row=20, column=2)
tkinter.Label(values, text="", bg="white").grid(column=4)
tkinter.Label(values, text="", bg="white").grid(row=21)
tkinter.Label(values, text="ID To Delete: ", font=("Franklin Gothic Book", 15, "bold"), bg="white", fg="#6cb444").grid(row=22, column=1)
delete_entry = tkinter.Entry(values, width=5, font=("Franklin Gothic Book", 15), borderwidth=1, relief="solid")
delete_entry.grid(row=22, column=2)
deleter_send = tkinter.Button(values, text="Delete", command=show_confirm, font=("Franklin Gothic Book", 15), bg="#6cb444", fg="white")
deleter_send.grid(row=22, column=3)
tkinter.Label(values, text="", height=3, bg="white").grid(row=23)
tkinter.Label(values, text="Id to Edit: ", font=("Franklin Gothic Book", 15, "bold"), bg="white", fg="#6cb444").grid(row=24, column=1)
edit_entry = tkinter.Entry(values, font=("Franklin Gothic Book", 15), width=5, borderwidth=1, relief="solid")
edit_entry.grid(row=24, column=2)
tkinter.Button(values, text="Edit", command=edit_value, font=("Franklin Gothic Book", 15), bg="#6cb444", fg="white").grid(row=24, column=3)
tkinter.Button(values, text="Back", command=show_manager, height=2, width=7, bg="dark gray").grid(column=10, row=0, sticky="n", padx=10, pady=4)
tkinter.Label(values, text="", width=2, bg="white").grid(row=0, column=8)
tkinter.Button(values, text="X", command=del_gui, width=7, height=2, bg="red").grid(column=11, row=0, pady=4, sticky="n")

# Creating edit employee details GUI
tkinter.Label(edit, text="", bg="white", width=77).grid(row=0, column=0)
edit_canvas = tkinter.Canvas(edit, width=350, height=150, highlightthickness=0, bg="white")
edit_canvas.grid(row=0, column=0, sticky="w")
edit_img = (Image.open("placeholder.jpg"))
edit_new_image = ImageTk.PhotoImage(master=edit_canvas, image=edit_img)
edit_canvas.create_image(40, 30, anchor="nw", image=edit_new_image)
tkinter.Label(edit, text="Edit Employee", font=("Franklin Gothic Book", 30), bg="white", fg="#6cb444").grid(row=1, column=2, pady=10)
tkinter.Label(edit, text="Full Name: ", width=10, font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=2, column=1)
name = tkinter.Entry(edit, width=20, font=("Franklin Gothic Book", 20))
name.grid(row=2, column=2)
tkinter.Label(edit, text="Contact No.: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=3, column=1)
phone = tkinter.Entry(edit, width=20, font=("Franklin Gothic Book", 20))
phone.grid(row=3, column=2)
tkinter.Label(edit, text="Email ID: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=4, column=1)
email = tkinter.Entry(edit, width=20, font=("Franklin Gothic Book", 20))
email.grid(row=4, column=2)
tkinter.Label(edit, text="Date of Birth: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=5, column=1)
edit_dob_frame = tkinter.Frame(edit, bg="white")
edit_dob_frame.grid(row=5, column=2, sticky="nsew")
edited_month_dob = tkinter.StringVar(edit_dob_frame)
edited_day_dob = tkinter.StringVar(edit_dob_frame)
edited_year_dob = tkinter.StringVar(edit_dob_frame)
tkinter.OptionMenu(edit_dob_frame, edited_month_dob, *months).pack(side=tkinter.LEFT)
tkinter.OptionMenu(edit_dob_frame, edited_day_dob, *days).pack(side=tkinter.LEFT, padx=64)
tkinter.OptionMenu(edit_dob_frame, edited_year_dob, *dob_years).pack(side=tkinter.LEFT)
tkinter.Label(edit, text="DOJ: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=6, column=1)
edit_doj_frame = tkinter.Frame(edit, bg="white")
edit_doj_frame.grid(row=6, column=2, sticky="nsew")
edited_month_doj = tkinter.StringVar(edit_doj_frame)
edited_day_doj = tkinter.StringVar(edit_doj_frame)
edited_year_doj = tkinter.StringVar(edit_doj_frame)
tkinter.OptionMenu(edit_doj_frame, edited_month_doj, *months).pack(side=tkinter.LEFT)
tkinter.OptionMenu(edit_doj_frame, edited_day_doj, *days).pack(side=tkinter.LEFT, padx=64)
tkinter.OptionMenu(edit_doj_frame, edited_year_doj, *doj_years).pack(side=tkinter.LEFT)

tkinter.Label(edit, text="Gender: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(column=1, row=7)
edited_sex = tkinter.StringVar(edit)
tkinter.OptionMenu(edit, edited_sex, *["Male", "Female", "Others"]).grid(column=2, row=7)
tkinter.Button(edit, text="Update", command=edit_button, font=("Franklin Gothic Book", 20), bg="#6cb444", fg="white").grid(column=2, row=8)
tkinter.Label(edit, text="", bg="white", width=45).grid(column=3)
tkinter.Button(edit, text="Back", command=show_all, height=2, width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(edit, text="X", bg="red", command=del_gui, width=7, height=2).grid(column=5, row=0, sticky="n", pady=4)


# Creating Enter Leaves GUI

# reads the current date
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
# creation of calendar to enter start date of leaves
tkinter.Label(cal_tk, text="", width=65, height=2, bg="white").grid(row=0, column=0)
cal_tk_canvas = tkinter.Canvas(cal_tk, width=350, height=150, highlightthickness=0, bg="white")
cal_tk_canvas.grid(row=0, column=0, sticky="w")
cal_tk_img = (Image.open("placeholder.jpg"))
cal_tk_new_image = ImageTk.PhotoImage(master=cal_tk_canvas, image=cal_tk_img)
cal_tk_canvas.create_image(40, 30, anchor="nw", image=cal_tk_new_image)
tkinter.Label(cal_tk, text="Leave Application", font=("Franklin Gothic Book", 22), bg="white").grid(row=1, column=2)
tkinter.Label(cal_tk, text="Leave Start", font=("Franklin Gothic Book", 15), bg="white").grid(row=2, column=1)
cal1 = Calendar(cal_tk, selectmode='day', year=year, month=month, day=day, font=("Franklin Gothic Book", 15))
cal1.grid(row=2, column=2)


# creation of calendar to enter end date of leaves
tkinter.Label(cal_tk, text="", bg="white").grid(row=3)
tkinter.Label(cal_tk, text="Leave End", font=("Franklin Gothic Book", 15), bg="white").grid(row=4, column=1)
cal2 = Calendar(cal_tk, selectmode='day', year=year, month=month, day=day, font=("Franklin Gothic Book", 15))
cal2.grid(row=4, column=2)
tkinter.Label(cal_tk, text="", bg="white", width=60).grid(column=3, row=5)
tkinter.Button(cal_tk, text="Enter", command=total_leave,
               font=("Franklin Gothic Book", 14), bg="#6cb444", fg="white").grid(row=6, column=2)
tkinter.Button(cal_tk, text="Back", command=show_employee, height=2,
               width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(cal_tk, text="X", command=del_gui, bg="red",
               width=7, height=2).grid(row=0, column=5, sticky="n", pady=4)

# Creating Change Password page GUI
tkinter.Label(new_password, text="", width=70, bg="white").grid(row=0, column=0)
password_canvas = tkinter.Canvas(new_password, width=350, height=150, highlightthickness=0, bg="white")
password_canvas.grid(row=0, column=0, sticky="w")
password_img = (Image.open("placeholder.jpg"))
password_new_image = ImageTk.PhotoImage(master=password_canvas, image=password_img)
password_canvas.create_image(40, 30, anchor="nw", image=password_new_image)

tkinter.Label(new_password, text="Original Password:", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=1, column=1)
og_password = tkinter.Entry(new_password, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid", show="*")
og_password.grid(row=1, column=2)
tkinter.Label(new_password, text="", bg="white").grid(row=2)
tkinter.Label(new_password, text="New Password: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=3, column=1)
created_password = tkinter.Entry(new_password, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid", show="*")
created_password.grid(row=3, column=2)
tkinter.Button(new_password, text="Enter", font=("Franklin Gothic Book", 20), command=create_password, bg="#6cb444", fg="white").grid(row=4, column=2)
tkinter.Label(new_password, text="", bg="white").grid(row=5)
tkinter.Label(new_password, text="", width=50, bg="white").grid(column=3)
tkinter.Button(new_password, text="Back", command=show_employee, height=2, width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(new_password, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=5, pady=4, sticky="n")

# Creating Main Budget page GUI
reader = open("total_budget.txt", "r")
fill_budget = reader.read()
tkinter.Label(budget, text="", width=60, bg="white").grid(column=0)
tkinter.Label(budget, text="", bg="white").grid(row=0, column=1)
budget_canvas = tkinter.Canvas(budget, width=350, height=150, highlightthickness=0, bg="white")
budget_canvas.grid(row=0, column=0, sticky="w")
budget_img = (Image.open("placeholder.jpg"))
budget_new_image = ImageTk.PhotoImage(master=budget_canvas, image=budget_img)
budget_canvas.create_image(40, 30, anchor="nw", image=budget_new_image)
tkinter.Label(budget, text="Budget Management", font=("Franklin Gothic Book", 30, "bold"), bg="white",  fg="#6cb444").grid(row=1, column=1)
tkinter.Label(budget, text="", height=2, bg="white").grid(row=2)
total_budget_frame = tkinter.Frame(budget, bg="white")
total_budget_frame.grid(row=3, column=1, padx=20)
tkinter.Label(total_budget_frame, text="Total Budget:", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").pack(side=tkinter.LEFT)
total_budget = tkinter.Entry(total_budget_frame, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
total_budget.pack(side=tkinter.LEFT, padx=20)
total_budget.insert(0, fill_budget)
tkinter.Button(total_budget_frame, text="Confirm", font=("Franklin Gothic Book", 20), command=update_total_budget, bg="#6cb444", fg="white")\
    .pack(side=tkinter.LEFT)
tkinter.Label(budget, text="", bg="white").grid(row=4)
tkinter.Button(budget, text="Add Salary", font=("Franklin Gothic Book", 20), fg="white", command=show_add_budget, bg="#6cb444", width=20)\
    .grid(row=5, column=0, sticky="e")
tkinter.Button(budget, text="Update Costs", font=("Franklin Gothic Book", 20), fg="white", command=show_update_budget, bg="#6cb444", width=20)\
    .grid(row=5, column=2, sticky="w")
tkinter.Label(budget, text="", bg="white").grid(row=6)
tkinter.Button(budget, text="Add Extra Costs", font=("Franklin Gothic Book", 20), fg="white", command=show_extra_costs, bg="#6cb444", width=20)\
    .grid(row=7, column=0, sticky="e")
tkinter.Button(budget, text="Budget Calculations", font=("Franklin Gothic Book", 20), fg="white", command=budget_show_all, bg="#6cb444", width=20)\
    .grid(row=7, column=2, sticky="w")
tkinter.Label(budget, text="", bg="white").grid(row=8)
tkinter.Button(budget, text="Back", command=show_manager, height=2, width=7, bg="dark gray").grid(column=5, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(budget, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=6, sticky="n", pady=4)


# Creating Add Salary page GUI
tkinter.Label(add_budget, text="", width=55, bg="white").grid(row=0, column=0)
tkinter.Label(add_budget, text="", width=35, bg="white").grid(row=0, column=1)
add_budget_canvas = tkinter.Canvas(add_budget, width=350, height=150, highlightthickness=0, bg="white")
add_budget_canvas.grid(row=0, column=0, sticky="w")
add_budget_img = (Image.open("placeholder.jpg"))
add_budget_new_image = ImageTk.PhotoImage(master=add_budget_canvas, image=add_budget_img)
add_budget_canvas.create_image(40, 30, anchor="nw", image=add_budget_new_image)
tkinter.Label(add_budget, text="Add Salary", font=("Franklin Gothic Book", 30), bg="white", fg="#6cb444").grid(row=1, column=2)
tkinter.Label(add_budget, text="", bg="white").grid(row=2, column=1)
tkinter.Label(add_budget, text="Employee ID:", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=3, column=1)
add_budget_id = tkinter.Entry(add_budget, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
add_budget_id.grid(row=3, column=2)
add_budget_id.bind("<FocusIn>", del_wrong_budget)
budget_wrong_id = tkinter.Entry(add_budget, font=('Franklin Gothic Book', 15), foreground="red", bg="white", borderwidth=0, highlightthickness=0)
budget_wrong_id.grid(row=3, column=3)
budget_wrong_id.insert(0, "This ID has been used")
budget_wrong_id.grid_forget()
tkinter.Label(add_budget, text="Salary:", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=4, column=1)
add_budget_quantity = tkinter.Entry(add_budget, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
add_budget_quantity.grid(row=4, column=2)
tkinter.Button(add_budget, text="Confirm", font=("Franklin Gothic Book", 20), fg="white",bg="#6cb444",
               command=employee_add_budget).grid(row=5, column=2)
tkinter.Label(add_budget, text="", bg="white").grid(row=6)
tkinter.Label(add_budget, text="", width=60, bg="white").grid(column=3)
tkinter.Button(add_budget, text="Back", command=show_budget, height=2, width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(add_budget, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=5, sticky="n", pady=4)

# Creating update salary and extra costs GUI
tkinter.Label(update_budget, text="", width=35, bg="white").grid(row=0, column=0)
update_budget_canvas = tkinter.Canvas(update_budget, width=350, height=150, highlightthickness=0, bg="white")
update_budget_canvas.grid(row=0, column=0, sticky="w")
update_budget_img = (Image.open("placeholder.jpg"))
update_budget_new_image = ImageTk.PhotoImage(master=update_budget_canvas, image=update_budget_img)
update_budget_canvas.create_image(40, 30, anchor="nw", image=update_budget_new_image)
tkinter.Label(update_budget, text="Update Employee Budget", font=("Franklin Gothic Book", 30), bg="white", fg="#6cb444").grid(row=1, column=2)
tkinter.Label(update_budget, text="", bg="white").grid(row=2, column=1)
tkinter.Label(update_budget, text="Employee ID: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=3, column=1)
update_budget_id = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
update_budget_id.grid(row=3, column=2)
tkinter.Button(update_budget, text="Check", font=("Franklin Gothic Book", 20), command=budget_update_setup, bg="#6cb444", fg="white").grid(row=3, column=3)
tkinter.Label(update_budget, text="Salary: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=4, column=1)
update_budget_quantity = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
update_budget_quantity.grid(row=4, column=2)
tkinter.Label(update_budget, text="Extra Cost: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=5, column=1)
update_extra_cost = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
update_extra_cost.grid(row=5, column=2)
tkinter.Label(update_budget, text="Cost Type: ", font=("Franklin Gothic Book", 20), bg="white", fg="#6cb444").grid(row=6, column=1)
update_cost_type = tkinter.Entry(update_budget, font=("Franklin Gothic Book", 20), bg="white", borderwidth=1, relief="solid")
update_cost_type.grid(row=6, column=2)
tkinter.Button(update_budget, text="Confirm", font=("Franklin Gothic Book", 20), fg="white",bg="#6cb444",
               command=employee_update_budget).grid(row=7, column=2)
tkinter.Label(update_budget, text="", width=49, bg="white").grid(column=4)
tkinter.Button(update_budget, text="Back", command=show_budget, height=2, width=7, bg="dark gray").grid(column=5, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(update_budget, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=6, sticky="n", pady=4)

# Creating Add Extra Costs page GUI
tkinter.Label(extra_costs, text="", width=75, bg="white").grid(row=0, column=0)
# adding an image on the top left of the page
extra_costs_canvas = tkinter.Canvas(extra_costs, width=350, height=150, highlightthickness=0, bg="white")
extra_costs_canvas.grid(row=0, column=0, sticky="w")
extra_costs_img = (Image.open("placeholder.jpg"))
extra_costs_new_image = ImageTk.PhotoImage(master=extra_costs_canvas, image=extra_costs_img)
extra_costs_canvas.create_image(40, 30, anchor="nw", image=extra_costs_new_image)
tkinter.Label(extra_costs, text="Add Extra Costs", font=("Franklin Gothic Book", 30), bg="white", fg="#6cb444").grid(row=1, column=2)
tkinter.Label(extra_costs, text="", bg="white").grid(row=2, column=1)
tkinter.Label(extra_costs, text="Employee ID: ", bg="white", fg="#6cb444", font=("Franklin Gothic Book", 20)).grid(row=3, column=1)
extra_cost_id = tkinter.Entry(extra_costs, font=("Franklin Gothic Book", 20), borderwidth=1,relief="solid")
extra_cost_id.grid(row=3, column=2)
tkinter.Label(extra_costs, text="Extra Cost", bg="white", fg="#6cb444", font=("Franklin Gothic Book", 20)).grid(row=4, column=1)
extra_costs_value = tkinter.Entry(extra_costs, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
extra_costs_value.grid(row=4, column=2)
tkinter.Label(extra_costs, text="Cost Type", bg="white", fg="#6cb444", font=("Franklin Gothic Book", 20)).grid(row=5, column=1)
extra_cost_type = tkinter.Entry(extra_costs, font=("Franklin Gothic Book", 20), borderwidth=1, relief="solid")
extra_cost_type.grid(row=5, column=2)
tkinter.Button(extra_costs, text="Confirm", font=("Franklin Gothic Book", 20), fg="white",bg="#6cb444",
               command=add_extra_costs).grid(row=6, column=2)
tkinter.Label(extra_costs, text="", width=52, bg="white").grid(column=3)
tkinter.Button(extra_costs, text="Back", command=show_budget, height=2, width=7, bg="dark gray").grid(column=4, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(extra_costs, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=5, sticky="n", pady=4)

# Creating budget calculations page GUI
tkinter.Canvas(budget_calculations, width=470, height=1, bg="white", highlightthickness=0).grid(row=0, column=0)
budget_calculations_canvas = tkinter.Canvas(budget_calculations, width=350, height=150, highlightthickness=0, bg="white")
budget_calculations_canvas.grid(row=0, column=0, sticky="w")
budget_calculations_img = (Image.open("placeholder.jpg"))
budget_calculations_new_image = ImageTk.PhotoImage(master=budget_calculations_canvas, image=budget_calculations_img)
budget_calculations_canvas.create_image(40, 30, anchor="nw", image=budget_calculations_new_image)
tkinter.Canvas(budget_calculations, width=181, height=1, bg="white", highlightthickness=0).grid(column=5)
# tkinter.Button(budget_calculations, text="Back", command=show_budget, height=2, width=7, bg="dark gray").grid(column=6, row=0, sticky="n", padx=10, pady=4)

# Creating View Leaves page GUI
tkinter.Label(show_leaves, width=50, bg="white").grid(row=0, column=0)
show_leaves_canvas = tkinter.Canvas(show_leaves, width=350, height=150, highlightthickness=0, bg="white")
show_leaves_canvas.grid(row=0, column=0, sticky="w")
show_leaves_img = (Image.open("placeholder.jpg"))
show_leaves_new_image = ImageTk.PhotoImage(master=show_leaves_canvas, image=show_leaves_img)
show_leaves_canvas.create_image(40, 30, anchor="nw", image=show_leaves_new_image)
tkinter.Label(show_leaves, text="", width=15, bg="white").grid(column=6)
tkinter.Button(show_leaves, text="Back", command=show_manager, height=2, width=7, bg="dark gray").grid(column=7, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(show_leaves, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=8, sticky="n", pady=4)

# Creating Enter Feedback page GUI
tkinter.Label(feedback, text="", width=60, bg="white").grid(row=0, column=0)
feedback_canvas = tkinter.Canvas(feedback, width=350, height=150, highlightthickness=0, bg="white")
feedback_canvas.grid(row=0, column=0, sticky="w")
feedback_img = (Image.open("placeholder.jpg"))
feedback_new_image = ImageTk.PhotoImage(master=feedback_canvas, image=feedback_img)
feedback_canvas.create_image(40, 30, anchor="nw", image=feedback_new_image)
tkinter.Label(feedback, text="", bg="white", width=10).grid(column=1)
tkinter.Label(feedback, text="Write Your Feedback", font=("Franklin Gothic Book", 20), bg="white").grid(row=1, column=2)
typed_feedback = tkinter.Entry(feedback, font=("Franklin Gothic Book", 20), width=40, borderwidth=1, relief="solid")
typed_feedback.grid(row=2, column=2)
tkinter.Label(feedback, text="", bg="white").grid(row=3)
tkinter.Button(feedback, font=("Franklin Gothic Book", 20), text="Submit", command=submit_feedback, bg="#6cb444").grid(row=4, column=2)
tkinter.Label(feedback, text="", bg="white", width=35).grid(column=4)
tkinter.Button(feedback, text="Back", command=show_employee, height=2, width=7, bg="dark gray").grid(column=5, row=0, sticky="n", padx=10, pady=4)
tkinter.Button(feedback, text="X", width=7, height=2, bg="red", command=del_gui).grid(row=0, column=6, sticky="n", pady=4)

# creating delete confirmation pop-up

tkinter.Label(confirmation, text="Are you sure you want to delete this employee?", fg="#6cb444", bg="white", font=("Franklin Gothic Book", 15, "bold")).pack(side="top", pady=15)
tkinter.Button(confirmation, text="No", command=show_all, fg="white", bg="red", font=("Franklin Gothic Book", 15), width=10).pack(side="left", padx=100)
tkinter.Button(confirmation, text="Yes", command=delete_confirm, bg="#6cb444", fg="white", font=("Franklin Gothic Book", 15), width=10).pack(side="right", padx=100)

login.mainloop()

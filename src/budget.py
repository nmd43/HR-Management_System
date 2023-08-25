import tkinter

budget = tkinter.Tk()
width = budget.winfo_screenwidth()
length = budget.winfo_screenheight()
budget.geometry("%dx%d" % (width, length))

tkinter.Label(budget, text="", width=35).grid(row=0, column=0)
tkinter.Label(budget, text="").grid(row=0, column=1)
tkinter.Label(budget, text="Budget Management", font=("Helvetica", 30)).grid(row=1, column=2)
tkinter.Label(budget, text="", height=12, width=65).grid(row=2, column=2)
tkinter.Button(budget, text="Add Employee Salary", font=("Helvetica", 20), fg="green").grid(row=3, column=1)
tkinter.Button(budget, text="Update Employee Salary", font=("Helvetica", 20), fg="green").grid(row=3, column=3)
tkinter.Label(budget, text="").grid(row=4)
tkinter.Button(budget, text="Enter Extra Costs", font=("Helvetica", 20), fg="green").grid(row=5, column=1)
tkinter.Button(budget, text="Budget Calculations", font=("Helvetica", 20), fg="green").grid(row=5, column=3)

budget.mainloop()
import functions
file = open("total_budget.txt", "r")

# variable = int(input("Type in your budget: "))
# print(variable)
# str_variable = repr(variable)
# file.write(str_variable)

read = file.read()
print(read)


class BudgetFunctions:
    def __init__(self):
        self.budgeter = functions.Budget(total_budget.get())
        total_budget.delete(0, tkinter.END)

    def employee_add_budget(self):
        self.budgeter.add_employee(add_budget_id.get(), add_budget_quantity.get())

    def employee_update_budget(self):
        self.budgeter.edit_employee(update_budget_id.get(), update_budget_quantity.get(), update_extra_cost.get(),
                                    update_cost_type.get())

    def add_extra_costs(self):
        self.budgeter.add_extra_costs(extra_cost_id.get(), int(extra_costs_value.get()), extra_cost_type.get())
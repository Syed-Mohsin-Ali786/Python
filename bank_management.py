# Admin
# add employees
# remove employees

# Manager
# viewing reports
# approving transaction

# Teller
# processing deposits
# withdraw process

# Clerk
# new account entry
# data updates


def user_input(prompt):
    return input(prompt).strip()


def adminRole():
    name = user_input("Enter admin name: ")
    password = user_input("Enter admin password: ")
    if name == "mohsin" and password == "2":
        print("Enter 1 to add employees: \nEnter 2 to remove an employee: ")
        adminOptions = user_input("Choice: ")
    else:
        print("invalid password or name")
        # Employees add
    if adminOptions == "1":
        while True:
            employee_id = user_input("Enter id of employee: ")
            if employee_id.isdigit():
                employee_id = int(employee_id)
                break
            print("Please enter only numbers")
        name = user_input("Name of employee: ")
        email = user_input("Email of employee: ")
        if employee_id and name and email:
            with open("./bank_managment/employees.txt", "r") as file:
                employees = file.readlines()
                for employee in employees:
                    if employee[0] == str(employee_id):
                        print("Id already exist")

                emplyee_list = [employee_id, "||", name, "||", email]

        with open("./bank_managment/employees.txt", "a") as employees:
            employees.writelines(emplyee_list)
        # Employees remove
    elif adminOptions == "2":
        while True:
            remove_id = user_input("Enter employee id: ")
            if remove_id.isdigit():
                break
            print("Please enter only numbers")
        with open("./bank_managment/employees.txt", "r") as employees:
            list_employee = employees.readlines()
            remove_list = []
            for employee in list_employee:
                data = employee.strip().split("||")
                if data[0] != remove_id:
                    remove_list.append(employee)
        with open("./bank_managment/employees.txt", "w") as employees:
            employees.writelines(remove_list)


def clerkRole():
    name = user_input("Enter clerk name: ")
    password = user_input("Enter clerk password: ")
    if name == "mohsin" and password == "2":
        print("Enter 1 to add user: \nEnter 2 to update user: ")
        adminOptions = user_input("Choice: ")
    else:
        print("invalid password or name")
        # new user add
    if adminOptions == "1":
        while True:
            employee_id = user_input("Enter id of employee: ")
            if employee_id.isdigit():
                employee_id = int(employee_id)
                break
            print("Please enter only numbers")
        name = user_input("Name of employee: ")
        email = user_input("Email of employee: ")
        if employee_id and name and email:
            with open("./bank_managment/employees.txt", "r") as file:
                employees = file.readlines()
                for employee in employees:
                    if employee[0] == str(employee_id):
                        print("Id already exist")

                emplyee_list = [employee_id, "||", name, "||", email]

        with open("./bank_managment/employees.txt", "a") as employees:
            employees.writelines(emplyee_list)
        # Employees remove
    elif adminOptions == "2":
        while True:
            remove_id = user_input("Enter employee id: ")
            if remove_id.isdigit():
                break
            print("Please enter only numbers")
        with open("./bank_managment/employees.txt", "r") as employees:
            list_employee = employees.readlines()
            remove_list = []
            for employee in list_employee:
                data = employee.strip().split("||")
                if data[0] != remove_id:
                    remove_list.append(employee)
        with open("./bank_managment/employees.txt", "w") as employees:
            employees.writelines(remove_list)


try:
    role = user_input("Enter your role: ")
    match role:
        case "admin":
            adminRole()
            print("this is completed")
        case "manager":
            print("this is not implemented")
        case "teller":
            print("this is not implemented")
        case "clerk":
            clerkRole()
except TypeError:
    print("type error")
except ValueError:
    print("value error")
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission error")
except Exception as e:
    print("the error: ", e)

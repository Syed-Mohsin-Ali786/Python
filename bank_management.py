# Admin
# add employees
# remove employees
# view employees

# Manager
# viewing reports
# approving transaction

# Teller
# processing deposits
# withdraw process

# Clerk
# new account entry of customers
# data updates

import os


def user_input(prompt):
    return input(prompt).strip()


def adminRole():
    print("==" * 5, "Please Login", "==" * 5)
    name = user_input("Enter admin name: ")
    password = user_input("Enter admin password: ")
    if name == "mohsin" and password == "2":
        while True:
            print("==" * 5, "Admin Pannel", "==" * 5)
            print(
                "Enter 1 to add employees: \nEnter 2 to remove an employee:  \nEnter 3 to view employees data:  \nEnter 0 to logout: "
            )
            adminOption = user_input("Choice: ")
            if adminOption == "0":
                return
            # Employees add
            if adminOption == "1":
                while True:
                    employee_id = user_input("Enter id of employee: ")
                    Exist = False
                    if employee_id.isdigit():
                        with open("./bank_managment/employees.txt", "r") as file:
                            for line in file:
                                # Split by your separator to get the first element accurately
                                parts = line.split("||")
                                if parts[0] == employee_id:
                                    Exist = True
                                    break
                        if Exist:
                            print("Id already exist")
                        else:
                            break
                    else:
                        print("Enter only digit")

                name = user_input("Name of employee: ")
                email = user_input("Email of employee: ")
                while True:
                    print("1. manager | 2. teller | 3. clerk")
                    choice = user_input("Choice: ")
                    match choice:
                        case "1":
                            role = "manager"
                            break
                        case "2":
                            role = "teller"
                            break
                        case "3":
                            role = "clerk"
                            break
                        case _:
                            print("Enter only the from the options")
                role_password = user_input("Enter the role_password: ")
                employee_data = (
                    f"{employee_id}||{name}||{email}||{role}||{role_password}\n"
                )
                with open("./bank_managment/employees.txt", "a") as employees:
                    employees.writelines(employee_data)
                    print("sucessfully added")
                # Employees remove
            elif adminOption == "2":
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
            # view employees
            elif adminOption == "3":
                with open("./bank_managment/employees.txt", "r") as employees:
                    list_employee = employees.readlines()

                    # 1. Print the Header
                    print("-" * 85)
                    print(
                        f"{'ID':<5} | {'Name':<15} | {'Email':<25} | {'Role':<10} | {'Password':<10}"
                    )
                    print("-" * 85)

                    for employee in list_employee:
                        data = employee.strip().split("||")

                        if len(data) == 5:
                            print(
                                f"{data[0]:<5} | {data[1]:<15} | {data[2]:<25} | {data[3]:<10} | {data[4]:<10}"
                            )

                    print("-" * 85)
    else:
        print("invalid password or name")
        input("Enter to continue ...")

    # To exit


def clerkRole():
    print("==" * 5, "login Pannel", "==" * 5)
    name = user_input("Enter clerk name: ")
    password = user_input("Enter clerk password: ")
    authorize = False
    with open("./bank_managment/employees.txt", "r") as file:
        employees = file.readlines()
        for employee in employees:
            employee_data = employee.strip().split("||")
            if employee_data[1] == name and employee_data[4] == password:
                authorize = True
        if authorize:
            print("==" * 5, "clerk Pannel", "==" * 5)
            print(
                "Enter 1 to add new account: \nEnter 2 to update data: \nEnter 3 to veiw data: "
            )
            clerOption = user_input("Choice: ")
        else:
            print("You are not authorize", "Error code 401")
        # new user add
    if clerOption == "1":
        while True:
            customer_id = user_input("Enter id of customer: ")
            if customer_id.isdigit():
                break
            else:
                print("Enter only number")
        name_customer = user_input("Name of customer: ")
        email_customer = user_input("Email of customer: ")
        total_amount = user_input("Enter the customer amount: $")
        if customer_id and name_customer and email_customer:
            if not os.path.exists("./bank_managment/customer.txt"):
                with open("./bank_managment/customer.txt", "x"):
                    pass

            customer_data = (
                f"{customer_id}||{name_customer}||{email_customer}||{total_amount}\n"
            )

        with open("./bank_managment/customer.txt", "a") as customers:
            customers.writelines(customer_data)
            print("success code 202")
        # Employees remove
    elif clerOption == "2":
        while True:
            customer_id = user_input("Enter employee id: ")
            if customer_id.isdigit():
                break
        print("Please enter only numbers")
        with open("./bank_managment/customer.txt", "r") as customers:
            list_customers = customers.readlines()
            isExist = False
            updated_list = []
            for customer in list_customers:
                data = customer.strip().split("||")
                if data[0] == customer_id:
                    isExist = True
                    print("1. ID | 2. Name | 3. Email | 4. Amount | 0. Cancel")
                    choice = user_input("What to update?: ")
                    match choice:
                        case "1":
                            data[0] = user_input("Enter new id: ")

                        case "2":
                            data[1] = user_input("Enter new name: ")

                        case "3":
                            data[2] = user_input("Enter new email: ")

                        case "4":
                            data[3] = user_input("Enter new amount: ")
                        case "0":
                            updated_list.append(data)
                            continue
                    updated_list.append(f"{data[0]}||{data[1]}||{data[2]}||{data[3]}\n")

                else:
                    updated_list.append(data)
            if isExist:
                with open("./bank_managment/customer.txt", "w") as file:
                    file.writelines(updated_list)
                    print("Update successful!")
            else:
                print("Customer ID not found.")
        # with open("./bank_managment/employees.txt", "w") as employees:
        #     employees.writelines(remove_list)
    elif clerOption == "3":
        with open("./bank_managment/customer.txt", "r") as customers:
            lines = customers.readlines()
            print("-" * 60)
            print(f"{'Id':<5}|{'Name':<10}|{'Email':<20}|{'Amount':<10}")
            print("-" * 60)
            for line in lines:
                data = line.strip().split("||")
                print(f"{data[0]:<5}|{data[1]:<10}|{data[2]:<20}|{data[3]:<10}")
            print("-" * 60)

            user_input("\nPress Enter to return to Clerk Panel...")
            return


while True:
    print("==" * 5, "Services Pannel", "==" * 5)
    print("admin: \nmanager: \nteller: \nclerk")
    role = user_input("Your role: ")
    try:
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

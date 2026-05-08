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


try:
    role = user_input("Enter your role: ")
    match role:
        case "admin":
            # name = input("Enter admin name: ")
            # password = input("Enter admin password: ")
            # if name == "mohsin" and password == "2":
            #     with open("./bank_managment/employees.txt", "a") as file:
            #         while True:
            #             name = user_input("Name of employee: ")
            #             email = user_input("Email of employee: ")
            #             if name and email:
            #                 data = [name, "||", email, "\n"]
            #                 file.writelines(data)
            #             print()
            #             break

            with open("./bank_managment/employees.txt", "r+") as employees:
                for index, employee in enumerate(employees):
                    employee_arry = employee.strip().splitlines()
                    employee_arry.insert(0, index)
                    print(employee_arry)

        # else:
        #     print("invalid password or name")
        case "manager":
            print("manager")
        case "teller":
            print("hello from tellor")
        case "clerk":
            print("this section is not implemented")
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

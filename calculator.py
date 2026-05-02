value1=float(input("Enter first number: "))
operator=input("Enter operator (*,/,-,+,%)")
value2=float(input("Enter second number: "))

match operator:
    case "+":
        result=value1 + value2
    case "-":
        result=value1 - value2
    case "*":
        result=value1 * value2
    case "/":
        result=value1 / value2
    case "%":
        result=value1 % value2
    case _:
        print("nothing")
print(f"Result of {value1} {operator} {value2} is {result}")

string=" """""""""""sdfakfopsdafsd"""""""""
# Task 1 Multiplication Table
# input_value=int(input("Enter a number: "))
# print(f"Table of {input_value}")
# print(f"{input_value}*1 = {input_value*1}")
# print(f"{input_value}*2 = {input_value*2}")
# print(f"{input_value}*3 = {input_value*3}")
# print(f"{input_value}*4 = {input_value*4}")
# print(f"{input_value}*5 = {input_value*5}")
# print(f"{input_value}*6 = {input_value*6}")
# print(f"{input_value}*7 = {input_value*7}")
# print(f"{input_value}*8 = {input_value*8}")
# print(f"{input_value}*9 = {input_value*9}")
# print(f"{input_value}*10 = {input_value*10}")

# Task 2 Arthematic Operations
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# print(f"Sum of {num1} and {num2} is {num1+num2}")
# print(f"Difference of {num1} and {num2} is {num1-num2}")
# print(f"Product of {num1} and {num2} is {num1*num2}")
# print(f"Quotient of {num1} and {num2} is {num1/num2}")
# print(f"Remainder of {num1} and {num2} is {num1%num2}")

# # Task 3 Comparison and Logical Expressions
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(f"Is {a} greater than {b} ? {a>b}")
# print(f"Is {a} less than {b} ? {a<b}")
# print(f"Is {a} equal to {b}  ? {a==b}")
# print(f"Is {a} not equal to {b}  ? {a!=b}")
# print(f"Is {a} greater than {b} and {a} is not equal to {b}  ? {(a>b) and (a!=b)}")
# print(f"Is {a} less than {b}  or {a} is equal to {b} ? {(a<b) or (a==b)}")

# name=str(input("Enter your name :"))
# age=int(input("Enter your age :"))
# language=str(input("Enter your language :"))

# print(" name :",name,"\n","age :",age,"\n","language :",language)
# profile={
#     "name":name,
#     "age":age,
#     "language":language
# }

# print(profile)

# number=12
# alpha='abcd'
# i=0
# while i<=number:
#     print(alpha[i])
#     i+=1


# fruits={"apple","mango"}
# # fruits.remove("ali")
# fruits.discard("ali")
# print(fruits)

# dis
# dis={
#     "name":"Ali",
#     "age":20,
#     "language":"Python"

# }

# # print(dis.get("name"))
# dis.__setitem__("language","Pakistan")
# dis.update({"age":21})s
# print(dis)

# fruits = ["apo dulla", "marzigon"]
# [x.upper() for x in fruits]
# print(fruits)
# for i in range(1, 5):
#     for j in range(1, 5):
#         print("*", end="")
#     print()

# input_value = int(input("Enter a number: "))

# isPrime = True

# if int(input_value**0.5) == input_value**0.5:
#     isPrime = False
#     print(f"{input_value} is not prime number")
#     exit()
# range_int = int(input_value**0.5) + 1
# for i in range(2, range_int):
#     if input_value % i == 0:
#         isPrime = False
#         break
# if isPrime:
#     print(f"{input_value} is prime number")
# else:
#     print(f"{input_value} is not prime number")
# num = int(input("Enter height of pyramid: "))

# for i in range(1,num + 1,2):

#     for j in range(num - i):
#         print(" ", end="")

#     for k in range(2 * i - 1):
#         print("*", end="")

#     # 3. Move to the next line
#     print()

# for i in range(1,num + 1):
#     spaces = " " * (num - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# userInput = int(input("Enter the range"))

# prime = []
# composite = []
# for i in range(1, userInput):
#     if int(userInput**0.5) == userInput**0.5:
#         composite.append(i)
#         for i in range(2, (userInput**0.5) + 1):
#             if i % 2 == 0:
#                 composite.append(i)
#     else:
#         prime.append(i)

# print(f"{composite} is composite number")
# print(f"{prime} is prime number")


# input_value = int(input("Enter a number: "))

# prime = []
# composite = []
# for num in range(1, input_value):
#     isPrime = True
#     if int(input_value**0.5) == input_value**0.5:
#         isPrime = False
#     exit()

#     range_int = int(num**0.5) + 1
#     for i in range(2, range_int):
#         if num % i == 0:
#             isPrime = False
#             break
# if isPrime:
#     print(f"{prime.append(num)}")
# else:
#     print(f"{composite.append(num)}")

# Task 1
# userInput = ""
# for i in range(1, 6):
#     userInput += input("Enter name of student: ") + "\n"

# with open("student.txt", "a") as f:
#     f.write(userInput)
# print("successfully added ")

# Task 2
with open("student.txt", "r") as f:
    count=0
    for line in f:
        words = line.strip().split()
        for word in words:
            print(word)
            count +=1
    print(count)
# Task 3

# for _ in range(2):
#     name = input("Enter two more student: ")
#     with open("student.txt", "a") as f:
#         f.write(f"{name}\n")

# Task 4
# for _ in range(3):
#     number = int(input("Enter a five number: "))
#     with open("number.txt", "a") as f:
#         f.write(f"{number}" + ",")
# with open("number.txt", "r") as f:
#     for number in f:
#         numbers = number.strip().split(",")
#     numbers_arry = [int(x) for x in numbers if x != ""]
#     Sum = 0
#     for i in range(0, len(numbers_arry)):
#         temp = Sum
#         Sum = int(numbers_arry[i]) + temp
#     average = Sum / len(numbers_arry)
#     print(f"{Sum} is the sum and {average} is the average")

# Task 5
# with open("student.txt", "r") as f:
#     for content in f:
#         with open("students_backup.txt", "a") as new:
#             new.write(content)
#     print("successfully added")
# best approage
# with open("student.txt", "r") as f, open("students_backup.txt", "w") as new:
#     for content in f:
#         new.write(content)
# print("Successfully backed up!")
# import shutil

# shutil.copy2("student.txt", "students_backup.txt")
# print("File copied successfully")
# Task 6
# with open("story.txt", "a") as file:
#     file.write("This is the altimate genrative ai course for deep learners ")
# with open("story.txt", "r") as story:
#     # print(story)
#     words_arry = story.read().split()
#     count_words = 0
#     count_letters = 0
#     for words in words_arry:
#         if words != "":
#             count_words += 1
#             for letter in words:
#                 count_letters += 1

#     print(count_words, count_letters)

# another way fastest
# with open("story.txt", "r") as story:
#     paragh = story.read()
#     words_arry = paragh.split()
#     print(len(words_arry))
#     letters = "".join(words_arry)
#     print(len(letters))

# def print_star(size=15):
#     # This loop iterates through y and x coordinates
#     for y in range(size, -size, -1):
#         line = ""
#         for x in range(-2 * size, 2 * size):
#             # Mathematical formula for a 5-pointed star (Simplified)
#             # Normalizing coordinates
#             nx, ny = x / size, y / size
            
#             # Using polar coordinates helps define the star points
#             import math
#             angle = math.atan2(nx, ny)
#             r = math.sqrt(nx**2 + ny**2)
            
#             # The "star" logic: 5-fold symmetry
#             # Adjusting the arms of the star
#             arm = math.cos(5 * angle)
#             star_shape = 0.5 + 0.3 * arm
            
#             if r < star_shape:
#                 line += "*"
#             else:
#                 line += " "
#         print(line)

# print_star(15)
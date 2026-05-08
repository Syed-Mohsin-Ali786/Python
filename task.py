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
# with open("student.txt", "r") as f:
#     count=0
#     for line in f:
#         words = line.strip().split()
#         for word in words:
#             print(word)
#             count +=1
#     print(count)
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
# def fileHandling():


# def ErrorHandler():
#     while True:
#         try:
#             role = input("Enter your name: ")
#             password = int(input("Enter a Password: ")).strip()
#             if role == "admin" and password == "1234":
#                 print("congratulations")
#                 break
#             else:
#                 print("You have entered wrong password or name")
#         except FileNotFoundError:
#             print("file not found")
#         except PermissionError:
#             print("permission denied")
#         except IsADirectoryError:
#             print("you oppend a directory instead of a file")
#         except (IOError, OSError):
#             print("Disk full or something regards to hardware")
#         except ValueError:
#             print("Invalid Operation on a file")
#         except Exception as e:
#             print("print", e)


# ErrorHandler()

from tkinter import *
import random

# --- CONFIGURATION ---
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        # Error handling for grid calculation
        try:
            x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        except ZeroDivisionError:
            print("Configuration Error: SPACE_SIZE cannot be zero.")
            window.destroy()


def next_turn(snake, food):
    try:
        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            global score
            score += 1
            label.config(text="Score:{}".format(score))
            canvas.delete("food")
            food = Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            # The 'after' call is wrapped in this try block to handle 
            # the case where the window is closed during the delay.
            window.after(SPEED, next_turn, snake, food)

    except TclError:
        # Handles errors when the window is closed while next_turn is pending
        pass
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    try:
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    except Exception:
        pass


# --- INITIALIZATION ---
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Center the window on screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind controls
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Start Game
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
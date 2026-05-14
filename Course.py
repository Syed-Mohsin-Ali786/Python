# # For Each Loop 1
# arry=['ali','muhammad','hassan','hussain']
# for item in arry:
#     print(item)
#     print(arry)
# print('done')

# #Finding the average of a list 2

# students_numbers=[1,2,3,4,5,6,7,8,9]
# i=0
# curr=0
# temp=0
# total=0
# length=len(students_numbers)
# while i<length:
#     curr += temp
#     temp= students_numbers[i]
#     i+=1
#     total=curr
# avg=total/length
# print(total,avg)

# Second way to find the average of a list

# student_height=input("Input a list of student height").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n]);
# print(student_height)

# total=0;
# for height in student_height:
#     total+=height
# print(total)

# le=0
# for student in student_height:
#     le+=1
# print(le)


# For highest score in a list 3
# student_height=input("Input a list of student height").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n]);
# print(student_height)

# cur=0;
# for height in student_height:
#     if height>cur:
#         cur=height
# print(cur)

# Range loop 4
# a=int(input("Enter your first number"))
# b=int(input("Enter your second number"))
# for number in range(a,b,2):
#     print(number)

# total=0;
# for number in range (1,101):
#     total += number
# print(total)

# toatl even number 5
# total=0;
# for number in range (1,101):
#     if number%2==0:
#      total += number
# print(total)

# another way to find total even number
# total=0;
# for number in range(2,101,2):
#     total += number
# print(total)

# fizz buzz game 6
# for number in range(1,101):
#  case1=number%3==0
#  case2=number%5==0

#  if case1 and case2:
#       print("fizzBuzz")
#  elif case1:
#       print("Buzz")
#  elif case2:
#       print("fizz")
#  else:
#       print({number})

# Password Generator 7
# Easy Level
# import random
# numbers = [5,4,3,4,5,6,7,8,9,10]
# letters = [
#     "a","b","c","d","e","f","g","h","i","j",
#     "k","l","m","n","o","p","q","r","s","t",
#     "u","v","w","x","y","z"
# ]
# symbols = [
#     "!","@","#","$","%","^","&","*","(",")",
#     "-","_","+","=","/","\\","|","?",";",":",
#     "'","\"","<",">",",","."
# ]

# print("Welcome to the PyPassword Generator")
# nr_numbers =int(input("How many numbers would you like in your password? \n"))
# nr_symbols =int(input("How many symbols would you like in your password? \n"))
# nr_letters =int(input("How many letters would you like in your password? \n"))

# gen_pass=""

# for number in range(1,nr_numbers + 1):
#    gen_pass += str(random.choice(numbers))
# for symbol in range(1,nr_symbols + 1):
#     gen_pass += str(random.choice(symbols))
# for letter in range(1,nr_letters + 1):
#     gen_pass += str(random.choice(letters))

# print(gen_pass)

# Hard level
# import random
# numbers = ["1","2","3","4","5","6","7","8","9","10"]
# letters = [
#     "a","b","c","d","e","f","g","h","i","j",
#     "k","l","m","n","o","p","q","r","s","t",
#     "u","v","w","x","y","z"
# ]
# symbols = [
#     "!","@","#","$","%","^","&","*","(",")",
#     "-","_","+","=","/","\\","|","?",";",":",
#     "'","\"","<",">",",","."
# ]

# print("Welcome to the PyPassword Generator")
# nr_numbers =int(input("How many numbers would you like in your password? \n"))
# nr_symbols =int(input("How many symbols would you like in your password? \n"))
# nr_letters =int(input("How many letters would you like in your password? \n"))

# gen_pass=[]

# for number in range(1,nr_numbers + 1):
#   gen_pass.append(random.choice(numbers))
# for symbol in range(1,nr_symbols + 1):
#   gen_pass.append(random.choice(symbols))
# for letter in range(1,nr_letters + 1):
#    gen_pass.append(random.choice(letters))

# random.shuffle(gen_pass)
# # password="".join(gen_pass)
# password=""
# for char in gen_pass:
#     password += char

# print(password)

# Random Word Game

# second method to generate random words
# words = ['apple', 'banana', 'cherry', 'dog', 'cat']
# random_word = random.choice(words)

# third method to generate random words
# from generalwords import get_words  # This works!

# words = get_words(n=10)  # Returns a tuple of words
# random_word = random.choice(words)
# print(random_word)
# first method to generate random words

# import random


# def start_game():
#     with open("words.txt", "r") as file:
#         words = file.read().splitlines()

#     target_word = random.choice(words)
#     print(target_word)

#     display_arry = list(("-") * len(target_word))
#     # for blank in range(0, len(target_word)):
#     #     display_arry.append("-")
#     lives = 9
#     while "-" in display_arry and lives > 0:
#         print("\n current word:", "".join(display_arry))

#         print("Lives remaining: ", lives)
#         user_guess = input("Guess a letter:").lower()
#         if user_guess in display_arry:
#             print(f"You have already guessed {user_guess}. Try a different letter.")
#         if user_guess in target_word:
#             for i in range(len(target_word)):
#                 if target_word[i] == user_guess:
#                     display_arry[i] = user_guess
#         else:
#             lives -= 1
#             print("Incorrect guess")
#     if lives > 0:
#         print("congratulationn you won: ", "".join(display_arry),"is correct word")
#     else:
#         print("Game over.You ran out of lives.")
#         print("The word was: ", target_word)


# start_game()

# def greet():
#     print("good")
#     print("excelent")
#     print("outstanding")

# greet()

# Area Calculation
# import math
# test_h = int(input("Enter the height of house: "))
# test_w = int(input("Enter the width of house: "))
# coverage = 5


# def area(test_h, test_w, coverage):
#     total_required = (test_h * test_w) / coverage
#     print(math.ceil(total_required))


# area(test_h, test_w, coverage)

# Caesar cypher
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(plain_text, shift_amount, cypher_direction):
    end_text = ""
    shift_amount %= 26
    if cypher_direction == "decode":
        shift_amount *= -1
    for char in plain_text:
        if char in letters:
            position = letters.index(char)
            new_postion = (position + shift_amount) % 26
            end_text += letters[new_postion]
        else:
            end_text += plain_text
    print(f"The {cypher_direction}d is {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # def caesar(start_text,shift_amount)
    # Encoding
    caesar(plain_text=text, shift_amount=shift, cypher_direction=direction)
    result = input("Enter Yes if you want to continue else No: ")
    if result == "No":
        print("Good bye")
        should_continue = False

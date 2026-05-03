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
import random

# first method to generate random words
# with open('words.txt','r') as file:
#   words = file.read().splitlines()

# random_word= random.choice(words)
# print(random_word)

# second method to generate random words
# words = ['apple', 'banana', 'cherry', 'dog', 'cat']
# random_word = random.choice(words)

# third method to generate random words
from generalwords import get_words  # This works!

words = get_words(n=10)  # Returns a tuple of words
random_word = random.choice(words)
print(random_word)

blanks = ""
for blank in range(0, len(random_word)):
    blanks += "-"

guess_word = ""
guess_letter = input("Guess a letter")


def true(i):
    blanks[i] = blanks[i].replace("_", guess_letter)


def check():
    i = 0
    for letter in random_word:
        if guess_letter == letter:
            true({i})
        i += 1


# while guess_word==random_word:

check()

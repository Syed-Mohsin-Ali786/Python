# a=3
# b=4
# print(a**b)
# print(a*"ali")

# print("hello world",end=" \n"*3)
# print("welcome to python programming")
# print(f"python is a great {"\t"*3}  language")
# print(False==0)

# account="12\n3"

# print(account*3)

# value=3.45
# value=round(value)
# print(value)

# a="ali",
# b=a="petter"
# print(a)

# imaginary=1+3j
# print (imaginary+3+2j)

# total_count= float(input("Enter the total count of students: "))
# discount_percent= float(input("Enter the discount percent: "))

# discount_amount= (discount_percent/100)*total_count
# discounted_price= total_count - discount_amount

# print(f"The discount amount is: {discounted_price}")

# list = ["ali","hassan","hussain"]
# string =" apo ".join(list)
# print(string)

# text=" hello. world . hello    "
# # print(text[-1:-5])
# # print (text[-1:-6:-1])

# real=text.replace("hello","real")
# # print (text.strip())
# print(text.split("."))


# formate
# text="My name is {},I love to {}"
# result=text.format("ali","reading book");
# print(result)

# f string
# name="ali"
# hobby="reading book"
# result=f"My name is {name},I love to {hobby}"

# shorthand if
# a = 4
# b = 6
# if a > b:
#     print("true")

# print("true") if a < b else print(True)

# while True:
#     name = input("Enter your name: ").strip()
#     password = input("Enter your password: ").strip()
#     if name == "admin" and password == "3215":
#         print("=" * 10 + "admin panel" + "=" * 10)
#         break
#     else:
#         print("Invalid email or password")

# import os

# while True:
#     print(
#         "Enter 1 add file: \nEnter 2 to view file: \nEnter 3 remove file: \nEnter 4 update file \nEnter 0 to exit: "
#     )
#     userInput = input("Choice: ")

#     match userInput:
#         case "0":
#             break
#         case "1":
#             print("add a file ")
#             with open("user_data.txt", "a") as file:
#                 name = input("Enter your name: ").strip()
#                 email = input("Enter your email: ").strip()
#                 age = input("Enter your age: ").strip()
#                 userData = [name, email, age]
#                 hanjee = "||".join(userData)
#                 if name and email and age:
#                     file.write(hanjee)
#                     break
#         case "4":
#             email = input("Enter your email: ")
#             with open("user_data.txt", "r") as f:
#                 isOpen = False
#                 student_list = f.readlines()
#                 print(student_list)
#                 for index, student in enumerate(student_list):
#                     record = student.strip().split()
#                     if record[1] == email:
#                         name = input("Enter Name")
#                         age = input("Enter age")
#                         student_list[index] = f"{name}||{email},{age}"
#                         isOpen = True
#                         break
#             if isOpen:
#                 with open("user_data.txt", "a") as file:
#                     file.writelines(student_list)
#                     print("successfully added")
#             else:
#                 print("file not opened")


# os.system("cls")

# def print_data(**dis):
#     print(dis)

# def print_list(*list):
#     print(list)

# # if you want to save function in a variable
# list_function=print_list
# print(list_function(3))


# class Students:
#     def __init__(self, name, roll_no, age=12):
#         self.name = name
#         self.age = age or 33
#         self.roll_no = roll_no
#         self.course="Gen AI"
#     def bio(self):
#         return self
#     def location(self):
#         return self

# first_student = Students("abid", "13 Gen AI")
# first_student.course="graphic"
# first_student.fatherName="father"

# f=Students("abid", "13 Gen AI")
# f.bio().name="abid chasmatop"
# f.location().located="baltistan"
# print(f.location().located)


# class Student:
#     def __init__(self, course, duration):
#         self.course = course
#         self.duration = duration

#     def bio(self, name, age):
#         self.name = name
#         self.age = age
#         return self

#     def purpose(self):
#         return self


# first_student = Student("Gen AI", "4 Month").bio("syed mohsin", 22)
# first_student.purpose().paragh = "To learn something"
# print(first_student.purpose().name)


# class office:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#     def branches(self):
#         return self
#     def
# office1 = office("akhwat", "faisalabad")
# office2 = office("nadra", "kursu")
# print(f"{office1.name}\n{office1.location}\n{office2.name}\n{office2.location}")


# class Student:
#     def __init__(self, course, duration):
#         self.course = course
#         self.duration = duration

#     def bio(self, name, age):
#         self.name = name
#         self.age = age
#         return self

#     def goal(self):
#         return self

#     def add(self):
#         self.age += 1
#         print(f"{self.age}")
#     def show(self):
#         print(self.age)


# second = Student("Gen AI", "4 month")

# fS = Student("Gen", "4 month").bio("Qamer", 40).goal()
# fS.goal().paragh = "to learn something"

# print(fS.add())
# print(fS.add())
# print(fS.add())
# print(fS.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = (name,)
#         self.age = age

#     def city(self):
#         self.location = "gazi abad"
#         return self


# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.section = "Gen AI"


# Student1 = Person("ali", 21).city()
# print(Student1.location)
# print(Student1.age)


# class Bird:
#     def fly(self):
#         self.name = "mohsin"
#         print("Birds can fly")
#         return self


# class Penguin(Bird):
#     def fly(self):
#         self.name="noman"
#         print("Penguins can't fly")
#         return self


# obj1 = Bird()

# obj2 = Penguin()

# print(obj1.fly().name, obj2.fly().name)

# class Shape:

#  def area(self):

#   pass

# class Circle(Shape):
 
#   def area(self):
 
#    print("Area of circle = πr²")
 
# class Rectangle(Shape):
 
#   def area(self):
 
#    print("Area of rectangle = l × w")
 
#  # Common interface
 
# for shape in [Circle(), Rectangle()]:
#     print(shape.area())


# class Computer:
#     def __init__(self):
#         self.CPU=self.CPU()
#         self.RAM=self.RAM()
#     class CPU:
#         def process(self):
#             work="process data"
#             return work
#     class RAM:
#         def store(self):
#             work="storing data"
#             return work
        
# computer=Computer()
# print(computer.CPU.process())
# print(computer.RAM.store())


